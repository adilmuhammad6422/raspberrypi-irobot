#include <iostream>
#include <fstream>
#include <chrono>
#include <thread>
#include <vector>
#include <cmath>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>

class Robot
{
public:
    Robot(const std::string &port = "/dev/ttyUSB0", int baudrate = B57600, int velocity = 200)
        : velocity(velocity)
    {
        tty_fd = open(port.c_str(), O_RDWR | O_NOCTTY);
        if (tty_fd == -1)
        {
            std::cerr << "Error opening serial port\n";
            exit(1);
        }
        struct termios tty;
        tcgetattr(tty_fd, &tty);
        cfsetospeed(&tty, baudrate);
        cfsetispeed(&tty, baudrate);
        tty.c_cflag |= (CLOCAL | CREAD);
        tcsetattr(tty_fd, TCSANOW, &tty);
    }

    ~Robot()
    {
        close(tty_fd);
    }

    void setVelocity(int velocity)
    {
        std::cout << "Setting velocity to: " << velocity << " mm/s\n";
        this->velocity = velocity;
    }

    void driveStraight()
    {
        std::cout << "Driving Straight...\n";
        callCommand(32768); // 32768 is the radius for driving straight
    }

    void turnDynamicAngle(double angle)
    {
        std::cout << "Turning " << angle << " degrees\n";
        double radius = (angle == 0) ? 32768 : 1 / (angle / 90.0);
        callCommand(static_cast<int>(radius));
        std::this_thread::sleep_for(std::chrono::milliseconds(static_cast<int>(abs(angle) / 90.0 * 1000)));
    }

    void stop()
    {
        writeCommand({137, 0, 0, 0, 0});
    }

    void start()
    {
        std::cout << "Starting the robot...\n";
        writeCommand({128, 132});
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    void detectBumper()
    {
        writeCommand({149, 1, 7}); // Request bumper sensor data
        uint8_t bump;
        read(tty_fd, &bump, 1);
        bool bump_right = bump & 0b00000001;
        bool bump_left = bump & 0b00000010;

        if (bump_left)
        {
            std::cout << "Left bumper pressed\n";
        }
        if (bump_right)
        {
            std::cout << "Right bumper pressed\n";
        }
    }

private:
    int tty_fd;
    int velocity;

    void writeCommand(const std::vector<uint8_t> &commands)
    {
        for (auto x : commands)
        {
            write(tty_fd, &x, 1);
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }

    void callCommand(int radius)
    {
        auto [vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte] = convertToBytes(velocity, radius);
        writeCommand({137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte});
    }

    std::tuple<uint8_t, uint8_t, uint8_t, uint8_t> convertToBytes(int velocity, int radius)
    {
        uint8_t vel_high_byte = (velocity >> 8) & 0xFF;
        uint8_t vel_low_byte = velocity & 0xFF;
        uint8_t radius_high_byte = (radius >> 8) & 0xFF;
        uint8_t radius_low_byte = radius & 0xFF;
        return {vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte};
    }
};

// Main function to call robot functions
int main()
{
    Robot robot;
    robot.start();
    robot.setVelocity(200);

    for (int i = 0; i < 10; ++i)
    { // Loop for N iterations, change 10 to N
        robot.detectBumper();
        std::this_thread::sleep_for(std::chrono::milliseconds(500)); // Delay between each iteration
    }

    return 0;
}
