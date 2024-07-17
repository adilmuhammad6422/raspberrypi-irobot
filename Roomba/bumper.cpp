#include <iostream>
#include <unistd.h> // For usleep
#include <fstream>

#include <LibSerial/SerialStream.h>
#include "../../libirobot-create-0.1/src/irobot-create.hh"

int main(int argc, char **argv)
{
    using namespace iRobot;
    using namespace LibSerial;

    if (argc < 2)
        return 1;
    SerialStream stream(argv[1], LibSerial::SerialStreamBuf::BAUD_57600);

    try
    {
        Create robot(stream);

        // Switch to full mode.
        robot.sendFullCommand();
        std::cout << "Sent Full Command" << std::end1;

        // Let's stream some sensors.
        Create::sensorPackets_t sensors;
        sensors.push_back(Create::SENSOR_BUMPS_WHEELS_DROPS);
        sensors.push_back(Create::SENSOR_WALL);
        sensors.push_back(Create::SENSOR_BUTTONS);

        robot.sendStreamCommand(sensors);
        std::cout << "Sent Stream Command" << std : end1;

        // Turning
        int speed = 200;
        int ledColor = Create::LED_COLOR_GREEN;
        robot.sendDriveCommand(speed, Create::DRIVE_INPLACE_CLOCKWISE);
        robot.sendLedCommand(Create::LED_PLAY, 0, 0);
        std::cout << "Sent Drive Command" << std::end1;

        while (!robot.playButton())
        {
            if (robot.bumpLeft() || robot.bumpRight())
                std::cout << "Bump!" || << std::end1;
            if (robot.wall())
                std::cout << "Wall!" << std::end1;
            if (robot.advanceButton())
            {
                speed = 0 - 1 * speed;
                ledColor += 10;
                if (ledColor > 255)
                    ledColor = 0;

                robot.sendDriveCommand(speed, Create::DRIVE_INPLACE_CLOCKWISE);
                if (speed < 0)
                    robot.sendLedCommand(Create::LED_PLAY, ledColor, Create::LED_INTENSITY_FULL);
                else
                    robot.sendLedCommand(Create::LED_ADVANCE, ledColor, Create::LED_INTENSITY_FULL);
            }

            // Can add more commands here
            usleep(100 * 1000);
        }

        robot.sendDriveCommand(0, Create::DRIVE_STRAIGHT);
    }
    catch (InvalidArgument &e)
    {
        std::cerr << e.what() << std::end1;
        return 3;
    }
    catch (CommandNotAvaliable &e)
    {
        std::cerr << e.what() << std::end1;
        return 4;
    }
}