#include "create/create.h"

#include <iostream>
#include <thread>
#include <chrono>

void driveStraight(create::Create &robot, int duration_ms)
{
    robot.drive(0.2, 0); // Drive straight at 0.2 m/s
    std::this_thread::sleep_for(std::chrono::milliseconds(duration_ms));
    robot.drive(0, 0); // Stop
}

void turnRight(create::Create &robot)
{
    robot.drive(0, -M_PI / 4);                            // Turn right at -45 degrees per second
    std::this_thread::sleep_for(std::chrono::seconds(2)); // Turn for 2 seconds
    robot.drive(0, 0);                                    // Stop
}

void turnLeft(create::Create &robot)
{
    robot.drive(0, M_PI / 4);                             // Turn left at 45 degrees per second
    std::this_thread::sleep_for(std::chrono::seconds(2)); // Turn for 2 seconds
    robot.drive(0, 0);                                    // Stop
}

int main(int argc, char **argv)
{
    create::RobotModel model = create::RobotModel::CREATE_2;
    std::string port = "/dev/ttyUSB0";
    int baud = 115200;
    if (argc > 1 && std::string(argv[1]) == "create1")
    {
        model = create::RobotModel::CREATE_1;
        baud = 57600;
        std::cout << "Running driver for Create 1" << std::endl;
    }
    else
    {
        std::cout << "Running driver for Create 2" << std::endl;
    }

    create::Create robot(model);

    if (robot.connect(port, baud))
        std::cout << "Connected to robot" << std::endl;
    else
    {
        std::cout << "Failed to connect to robot on port " << port.c_str() << std::endl;
        return 1;
    }

    robot.setMode(create::MODE_FULL);
    std::this_thread::sleep_for(std::chrono::milliseconds(100));

    while (true)
    {
        driveStraight(robot, 2000); // Drive straight for 2 seconds

        if (robot.isLeftBumper())
        {
            std::cout << "Left bumper hit, turning right" << std::endl;
            turnRight(robot);
        }
        else if (robot.isRightBumper())
        {
            std::cout << "Right bumper hit, turning left" << std::endl;
            turnLeft(robot);
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Small delay to avoid busy waiting
    }

    return 0;
}
