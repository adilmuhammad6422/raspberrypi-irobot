#!/bin/bash
cd Roomba
g++ -o client client.cpp -I/usr/local/include -L/usr/local/lib -lcreate -pthread
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
./client