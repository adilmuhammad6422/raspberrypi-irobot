#include "create/create.h"
#include <iostream>
#include <iomanip>
#include <thread>
#include <chrono>


// This file creates a class to communicate with the roomba. 

// The main method runs a good sanity check that the pi is communicating with the roomba. 
// Roomba will go forward for a total of 45 seconds while
//      turning left or right if it bumps into an obstacle on its left or right respectively.
//      turning around if it detects a virtual wall.

// TODO: 
// 1. in-place turning left 360.
// 2. in-place turning right 360.
// 3. reversing

class RobotDriver
{
public:
    RobotDriver(create::RobotModel model, const std::string &port, int baud)
        : robot_(model), port_(port), baud_(baud), interrupt_(false) {}

    bool connect()
    {
        if (robot_.connect(port_, baud_))
        {
            std::cout << "Connected to robot" << std::endl;
            robot_.setMode(create::MODE_FULL);
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            return true;
        }
        else
        {
            std::cout << "Failed to connect to robot on port " << port_ << std::endl;
            return false;
        }
    }

    void driveStraight(double velocity)
    {
        robot_.drive(velocity, 0.0);
    }

    void stop()
    {
        interrupt_ = true; // set interrupt to true 
        std::this_thread::sleep_for(std::chrono::milliseconds(50)); // sleep for 50ms so that loops stop due to interrupt=true
        robot_.drive(0.0, 0.0); // stop roomba
    }

    void turn(double leftWheelVelocity, double rightWheelVelocity, int duration_ms)
    {
        robot_.driveWheels(leftWheelVelocity, rightWheelVelocity);
        std::this_thread::sleep_for(std::chrono::milliseconds(duration_ms));
        stop();
    }

    void run(int duration_s)
    {
        interrupt_ = false;
        driveStraight(0.2);

        auto start_time = std::chrono::steady_clock::now();
        auto duration = std::chrono::seconds(duration_s);

        while (!interrupt_ && std::chrono::steady_clock::now() - start_time < duration)
        {

            if (robot_.isLeftBumper())
            {
                turn(0.15, -0.15, 1000); // Turn right
                driveStraight(0.2);      // Resume driving straight after turn
            }
            else if (robot_.isRightBumper())
            {
                turn(-0.15, 0.15, 1000); // Turn left
                driveStraight(0.2);      // Resume driving straight after turn
            }
            else if (robot_.isVirtualWall())
            {
                turn(-0.2, 0.2, 2000); // turn 180 degrees to the left (adjust timing to change)
                std::cout << "Virtual wall detected. Turning 180 degrees." << std::endl;
                driveStraight(0.2);
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }

        stop(); // Stop the robot after 45 seconds
    }

    // Debugging code:
    void testVirtualWall(int duration_s)
    {
        auto start_time = std::chrono::steady_clock::now();
        auto duration = std::chrono::seconds(duration_s);

        driveStraight(0.2);
        while (std::chrono::steady_clock::now() - start_time < duration)
        {
            if (robot_.isVirtualWall())
            {
                turn(-0.2, 0.2, 2000); // turn 180 degrees to the left (adjust timing to change)
                std::cout << "Virtual wall detected. Turning 180 degrees." << std::endl;
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
    }

private:
    create::Create robot_;
    std::string port_;
    int baud_;
    bool interrupt_;
};

int main(int argc, char **argv)
{
    create::RobotModel model = create::RobotModel::CREATE_1;
    std::string port = "/dev/ttyUSB0";
    int baud = 57600;
    std::cout << "Running driver for Create 1" << std::endl;

    RobotDriver driver(model, port, baud);
    if (!driver.connect())
    {
        return 1;
    }

    driver.run(5);

    return 0;
}
