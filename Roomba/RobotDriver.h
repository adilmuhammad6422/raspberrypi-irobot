#ifndef ROBOT_DRIVER_H
#define ROBOT_DRIVER_H

#include "create/create.h"
#include <iostream>
#include <iomanip>
#include <thread>
#include <chrono>
#include <string>
#include <atomic>
#include <condition_variable>
#include <mutex>

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

    void run() {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            running_ = true; // Set the running flag to true to start the loop
        }
        std::thread(&RobotDriver::runLoop, this).detach(); // Run the loop in a separate thread
    }

    void testVirtualWall() {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            running_ = true; // Set the running flag to true to start the loop
        }
        std::thread(&RobotDriver::virtualWallLoop, this).detach(); // Run the loop in a separate thread
    }

private:
    void runLoop() {
        driveStraight(0.2);
        bool contact_bumpers[2] = {false, false};

        while (true) {
            {
                std::lock_guard<std::mutex> lock(mutex_);
                if (!running_) break; // Exit loop if not running
            }

            contact_bumpers[0] = robot_.isLeftBumper();
            contact_bumpers[1] = robot_.isRightBumper();

            if (contact_bumpers[0]) {
                turn(0.15, -0.15, 1000);  // Turn right
                driveStraight(0.2);  // Resume driving straight after turn
            } else if (contact_bumpers[1]) {
                turn(-0.15, 0.15, 1000);  // Turn left
                driveStraight(0.2);  // Resume driving straight after turn
            } else if(robot_.isVirtualWall()) {
                turn(-0.2, 0.2, 2000); // turn 180 degrees to the left (adjust timing to change)
                std::cout << "Virtual wall detected. Turning 180 degrees." << std::endl;
                driveStraight(0.2);
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
