#ifndef ROBOT_DRIVER_H
#define ROBOT_DRIVER_H

#include "create/create.h"
#include <iostream>
// #include <iomanip>
#include <thread>
#include <chrono>
#include <string>
#include <atomic>
#include <condition_variable>
#include <mutex>
#include <random>
#include <cmath>

class RobotDriver {
public:
    RobotDriver(create::RobotModel model, const std::string& port, int baud)
        : robot_(model), port_(port), baud_(baud), running_(false) {}

    bool connect() {
        if (robot_.connect(port_, baud_)) {
            std::cout << "Connected to robot" << std::endl;
            robot_.setMode(create::MODE_FULL);
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            return true;
        } else {
            std::cout << "Failed to connect to robot on port " << port_ << std::endl;
            return false;
        }
    }

    void driveStraight(double velocity) {
        robot_.drive(velocity, 0.0);
    }

    void stop() {
        std::lock_guard<std::mutex> lock(mutex_);
        running_ = false; // Set the running flag to false to stop the run method
        robot_.drive(0.0, 0.0);
        cv_.notify_all();
    }

    void turn(double leftWheelVelocity, double rightWheelVelocity, int duration_ms) {
        robot_.driveWheels(leftWheelVelocity, rightWheelVelocity);
        std::this_thread::sleep_for(std::chrono::milliseconds(duration_ms));
        robot_.drive(0.0, 0.0); // Stop after turn
    }

    void run(int roomba_speed_cm=2) {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            running_ = true; // Set the running flag to true to start the loop
        }
        double m_speed = static_cast<double>(roomba_speed_cm)/10.0;
        std::thread(&RobotDriver::runLoop, this, m_speed).detach(); // Run the loop in a separate thread
    }

    void LeftRightTurn(){
        turn(0.15, -0.15, 1000);  // Turn right
        turn(-0.15, +0.15, 2000);  // Turn left
        turn(0.15, -0.15, 1000);  // face front
    }

    void testVirtualWall() {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            running_ = true; // Set the running flag to true to start the loop
        }
        std::thread(&RobotDriver::virtualWallLoop, this).detach(); // Run the loop in a separate thread
    }

private:
    void runLoop(double roomba_speed) {
        std::random_device rd;
        std::mt19937 gen(rd());

        std::normal_distribution<double> vw_noise(0.0, 0.2); // this translates into noise that 87% will turn the roomba +- 30 degrees of original turning amount
        std::normal_distribution<double> bumper_noise(0.0, 0.05); // this translates into noise that 83% will turn the roomba +- 5 degrees of original turning amount
        
        driveStraight(roomba_speed);
        bool contact_bumpers[2] = {false, false};

        while (true) {
            {
                std::lock_guard<std::mutex> lock(mutex_);
                if (!running_) break; // Exit loop if not running
            }

            contact_bumpers[0] = robot_.isLeftBumper();
            contact_bumpers[1] = robot_.isRightBumper();
            int ms_turning_time = 0;
            if (contact_bumpers[0]) {
                ms_turning_time = 675 + std::round(bumper_noise(gen)*1000); // turn 180 degrees to the left. 675 ms to turn 45. 
                turn(0.15, -0.15, ms_turning_time);  // Turn right. 675 ms needed to turn 45 degrees at that speed
                driveStraight(roomba_speed);  // Resume driving straight after turn
            } else if (contact_bumpers[1]) {
                ms_turning_time = 675 + std::round(bumper_noise(gen)*1000); // turn 180 degrees to the left. 675 ms to turn 45. 
                turn(-0.15, 0.15, ms_turning_time);  // Turn left. 675 ms needed to turn 45 degrees at that speed
                driveStraight(roomba_speed);  // Resume driving straight after turn
            } else if(robot_.isVirtualWall()) {
                ms_turning_time = 2025 + std::round(vw_noise(gen)*1000); // turn 180 degrees to the left. 2025 ms to turn 180. 
                turn(-0.2, 0.2, ms_turning_time); 
                // std::cout << "Virtual wall detected. Turning 180 degrees." << std::endl;x
                driveStraight(roomba_speed);
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }

    void virtualWallLoop() {
        driveStraight(0.2);
        while (true) {
            {
                std::lock_guard<std::mutex> lock(mutex_);
                if (!running_) break; // Exit loop if not running
            }

            if (robot_.isVirtualWall()) {
                turn(-0.2, 0.2, 2000); // turn 180 degrees to the left (adjust timing to change)
                std::cout << "Virtual wall detected. Turning 180 degrees." << std::endl;
                driveStraight(0.2);
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }

    create::Create robot_;
    std::string port_;
    int baud_;
    std::atomic<bool> running_; // Atomic flag to control the loop execution
    std::condition_variable cv_;
    std::mutex mutex_;
};

#endif // ROBOT_DRIVER_H
