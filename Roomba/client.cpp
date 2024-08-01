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
    const char *host = "192.168.1.100"; // Replace with your server's IP address
    int port = 44700;

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
    server_addr.sin_port = htons(port);
    inet_pton(AF_INET, host, &server_addr.sin_addr);

    // Connect to the server
    if (connect(client_socket, (sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        std::cerr << "Connection failed\n";
        close(client_socket); // Close the socket on failure
        return 1;
    }

    // Robot stuff here

    char buffer[1024];
    while (true)
    {
        memset(buffer, 0, sizeof(buffer));
        int bytes_received = recv(client_socket, buffer, sizeof(buffer) - 1, 0);
        if (bytes_received < 0)
        {
            std::cerr << "Recv failed\n";
            break;
        }
        else if (bytes_received == 0)
        {
            std::cout << "Server closed connection\n";
            break;
        }

        std::string response(buffer);
        std::cout << "Received: " << response << "\n";

        std::string command = response.substr(0, response.find(' '));
        int param1 = 0, param2 = 0;
        sscanf(response.c_str(), "%*s %d %d", &param1, &param2); // Using sscanf to parse the parameters

        std::string send_command;
        if (command == "straight")
        {
            send_command = "straight";
            // Implement here

        }
        else if (command == "stop")
        {
            send_command = "stop";
            // Implement here
        }
        else if (command == "forward_with_bump")
        {
            send_command = "forward_with_bump";
            // Implement here
        }

        if (!send_command.empty()) {
            send(client_socket, send_command.c_str(), send_command.size(), 0);
        }
    }

    close(client_socket);
    return 0;
}
