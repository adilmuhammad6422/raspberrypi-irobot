#include "create/create.h"

#include <iomanip>
#include <iostream>

int main(int argc, char **argv)
{
    // Make Create 1 robot
    create::RobotModel model = create::RobotModel::CREATE_1;
    std::string port = "/dev/ttyUSB0";
    int baud = 57600;
    std::cout << "Running driver for Create 1" << std::endl;

    // Construct robot object
    create::Create robot(model);

    // Connect to robot
    if (robot.connect(port, baud))
        std::cout << "Connected to robot" << std::endl;
    else
    {
        std::cout << "Failed to connect to robot on port " << port.c_str() << std::endl;
        return 1;
    }

    // Switch to Full mode
    robot.setMode(create::MODE_FULL);

    // There's a delay between switching modes and when the robot will accept drive commands
    usleep(100000);

    // Command robot to drive a radius of 0.15 metres at 0.2 m/s
    robot.drive(2, 0);

    // robot.driveRadius(0.2, 0.15);

    while (true)
    {
        // Get robot odometry and print
        const create::Pose pose = robot.getPose();

        std::cout << std::fixed << std::setprecision(2) << "\rOdometry (x, y, yaw): ("
                  << pose.x << ", " << pose.y << ", " << pose.yaw << ")      ";

        usleep(10000); // 10 Hz
    }

    return 0;
}