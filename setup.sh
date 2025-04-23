sudo apt-get install build-essential cmake libboost-system-dev libboost-thread-dev
sudo usermod -a -G dialout $USER
cd Roomba
mkdir build && cd build
cmake ..
make
sudo make install
cd ..
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
g++ -o roomba_bumper roomba_bumper.cpp -I/usr/local/include -L/usr/local/lib -lcreate
g++ -o client client.cpp -I/usr/local/include -L/usr/local/lib -lcreate -pthread