// RobotDriver.h
#ifndef ROBOT_DRIVER_H
#define ROBOT_DRIVER_H

#include "create/create.h"
#include <iostream>
#include <iomanip>
#include <thread>
#include <chrono>

class RobotDriver {
public:
    RobotDriver(create::RobotModel model, const std::string& port, int baud)
        : robot_(model), port_(port), baud_(baud) {}

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
        robot_.drive(0.0, 0.0);
    }

    void turn(double leftWheelVelocity, double rightWheelVelocity, int duration_ms) {
        robot_.driveWheels(leftWheelVelocity, rightWheelVelocity);
        std::this_thread::sleep_for(std::chrono::milliseconds(duration_ms));
        driveStraight(0.2);  // Resume driving straight after turn
    }

    void run() {
        driveStraight(0.2);
        bool contact_bumpers[2] = {false, false};

        while (true) {
            contact_bumpers[0] = robot_.isLeftBumper();
            contact_bumpers[1] = robot_.isRightBumper();

            if (contact_bumpers[0]) {
                turn(0.15, -0.15, 1000);  // Turn right
            } else if (contact_bumpers[1]) {
                turn(-0.15, 0.15, 1000);  // Turn left
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }

private:
    create::Create robot_;
    std::string port_;
    int baud_;
};

#endif // ROBOT_DRIVER_H
