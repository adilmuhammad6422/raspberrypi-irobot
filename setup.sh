sudo apt-get install build-essential cmake libboost-system-dev libboost-thread-dev
sudo usermod -a -G dialout $USER
cd Roomba
mkdir build && cd build
cmake ..
make
sudo make install
cd ..
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
g++ -static -o client client.cpp /usr/local/lib/libcreate.a -I/usr/local/include -lboost_system -lboost_thread -lpthread