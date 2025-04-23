#include "RobotDriver.h"
#include <iostream>
#include <string>
#include <cstring>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstdio> // Include this for sscanf

int main()
{
    // Server details
    const char *server_host = "192.168.1.110"; // Replace with your server's IP address
    int server_port = 44700;

    // Create a socket
    int client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket == -1)
    {
        std::cerr << "Could not create socket\n";
        return 1;
    }

    // Setup server address
    sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port);
    inet_pton(AF_INET, server_host, &server_addr.sin_addr);

    // Connect to the server
    if (connect(client_socket, (sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        std::cerr << "Connection failed\n";
        close(client_socket); // Close the socket on failure
        return 1;
    }

    // Initialize RobotDriver
    create::RobotModel model = create::RobotModel::CREATE_1;
    std::string robot_port = "/dev/ttyUSB0";
    int baud = 57600;
    RobotDriver driver(model, robot_port, baud);
    if (!driver.connect()) {
        close(client_socket);
        return 1;
    }

    char buffer[1024];
    while (true)
    {
        memset(buffer, 0, sizeof(buffer));
        int bytes_received = recv(client_socket, buffer, sizeof(buffer) - 1, 0);
        if (bytes_received < 0){
            std::cerr << "Recv failed\n";
            break;
        }else if (bytes_received == 0){
            std::cout << "Server closed connection\n";
            break;
        }

        std::string response(buffer);
        std::cout << "Received: " << response << "\n";

        std::string command = response.substr(0, response.find(' '));
        double param1 = 0.0, param2 = 0.0;
        sscanf(response.c_str(), "%*s %lf %lf", &param1, &param2); // Using sscanf to parse the parameters

        std::string send_command;
        if (command == "straight"){
            driver.driveStraight(param1); // go straight at param1 mm/s
            send_command = "Going straight...";
        }else if (command == "stop"){
            driver.stop();
            send_command = "Stopping...";
        }else if (command == "turn"){
            driver.turn(param1, param2, 1000); // param1 and param2 are wheel velocities
            send_command = "Turning...";
        }else if (command == "runDemo"){
            driver.run(param1);
            send_command = "Running Demo...";
        }else if (command == "testWall"){
            driver.testVirtualWall();
            send_command = "Testing Virtual Wall...";
        }else if (command == "hello"){
            send_command = "Hello!";
        }

        if (!send_command.empty()) {
            send(client_socket, send_command.c_str(), send_command.size(), 0);
        }
    }

    close(client_socket);
    return 0;
}
