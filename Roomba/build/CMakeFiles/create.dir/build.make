# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/raspberrypi/libcreate

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/raspberrypi/libcreate/build

# Include any dependencies generated for this target.
include CMakeFiles/create.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/create.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/create.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/create.dir/flags.make

CMakeFiles/create.dir/src/create.cpp.o: CMakeFiles/create.dir/flags.make
CMakeFiles/create.dir/src/create.cpp.o: /home/raspberrypi/libcreate/src/create.cpp
CMakeFiles/create.dir/src/create.cpp.o: CMakeFiles/create.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/create.dir/src/create.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/create.dir/src/create.cpp.o -MF CMakeFiles/create.dir/src/create.cpp.o.d -o CMakeFiles/create.dir/src/create.cpp.o -c /home/raspberrypi/libcreate/src/create.cpp

CMakeFiles/create.dir/src/create.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/create.dir/src/create.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/src/create.cpp > CMakeFiles/create.dir/src/create.cpp.i

CMakeFiles/create.dir/src/create.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/create.dir/src/create.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/src/create.cpp -o CMakeFiles/create.dir/src/create.cpp.s

CMakeFiles/create.dir/src/serial.cpp.o: CMakeFiles/create.dir/flags.make
CMakeFiles/create.dir/src/serial.cpp.o: /home/raspberrypi/libcreate/src/serial.cpp
CMakeFiles/create.dir/src/serial.cpp.o: CMakeFiles/create.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/create.dir/src/serial.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/create.dir/src/serial.cpp.o -MF CMakeFiles/create.dir/src/serial.cpp.o.d -o CMakeFiles/create.dir/src/serial.cpp.o -c /home/raspberrypi/libcreate/src/serial.cpp

CMakeFiles/create.dir/src/serial.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/create.dir/src/serial.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/src/serial.cpp > CMakeFiles/create.dir/src/serial.cpp.i

CMakeFiles/create.dir/src/serial.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/create.dir/src/serial.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/src/serial.cpp -o CMakeFiles/create.dir/src/serial.cpp.s

CMakeFiles/create.dir/src/serial_stream.cpp.o: CMakeFiles/create.dir/flags.make
CMakeFiles/create.dir/src/serial_stream.cpp.o: /home/raspberrypi/libcreate/src/serial_stream.cpp
CMakeFiles/create.dir/src/serial_stream.cpp.o: CMakeFiles/create.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/create.dir/src/serial_stream.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/create.dir/src/serial_stream.cpp.o -MF CMakeFiles/create.dir/src/serial_stream.cpp.o.d -o CMakeFiles/create.dir/src/serial_stream.cpp.o -c /home/raspberrypi/libcreate/src/serial_stream.cpp

CMakeFiles/create.dir/src/serial_stream.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/create.dir/src/serial_stream.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/src/serial_stream.cpp > CMakeFiles/create.dir/src/serial_stream.cpp.i

CMakeFiles/create.dir/src/serial_stream.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/create.dir/src/serial_stream.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/src/serial_stream.cpp -o CMakeFiles/create.dir/src/serial_stream.cpp.s

CMakeFiles/create.dir/src/serial_query.cpp.o: CMakeFiles/create.dir/flags.make
CMakeFiles/create.dir/src/serial_query.cpp.o: /home/raspberrypi/libcreate/src/serial_query.cpp
CMakeFiles/create.dir/src/serial_query.cpp.o: CMakeFiles/create.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/create.dir/src/serial_query.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/create.dir/src/serial_query.cpp.o -MF CMakeFiles/create.dir/src/serial_query.cpp.o.d -o CMakeFiles/create.dir/src/serial_query.cpp.o -c /home/raspberrypi/libcreate/src/serial_query.cpp

CMakeFiles/create.dir/src/serial_query.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/create.dir/src/serial_query.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/src/serial_query.cpp > CMakeFiles/create.dir/src/serial_query.cpp.i

CMakeFiles/create.dir/src/serial_query.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/create.dir/src/serial_query.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/src/serial_query.cpp -o CMakeFiles/create.dir/src/serial_query.cpp.s

CMakeFiles/create.dir/src/data.cpp.o: CMakeFiles/create.dir/flags.make
CMakeFiles/create.dir/src/data.cpp.o: /home/raspberrypi/libcreate/src/data.cpp
CMakeFiles/create.dir/src/data.cpp.o: CMakeFiles/create.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/create.dir/src/data.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/create.dir/src/data.cpp.o -MF CMakeFiles/create.dir/src/data.cpp.o.d -o CMakeFiles/create.dir/src/data.cpp.o -c /home/raspberrypi/libcreate/src/data.cpp

CMakeFiles/create.dir/src/data.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/create.dir/src/data.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/src/data.cpp > CMakeFiles/create.dir/src/data.cpp.i

CMakeFiles/create.dir/src/data.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/create.dir/src/data.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/src/data.cpp -o CMakeFiles/create.dir/src/data.cpp.s

CMakeFiles/create.dir/src/packet.cpp.o: CMakeFiles/create.dir/flags.make
CMakeFiles/create.dir/src/packet.cpp.o: /home/raspberrypi/libcreate/src/packet.cpp
CMakeFiles/create.dir/src/packet.cpp.o: CMakeFiles/create.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/create.dir/src/packet.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/create.dir/src/packet.cpp.o -MF CMakeFiles/create.dir/src/packet.cpp.o.d -o CMakeFiles/create.dir/src/packet.cpp.o -c /home/raspberrypi/libcreate/src/packet.cpp

CMakeFiles/create.dir/src/packet.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/create.dir/src/packet.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/src/packet.cpp > CMakeFiles/create.dir/src/packet.cpp.i

CMakeFiles/create.dir/src/packet.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/create.dir/src/packet.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/src/packet.cpp -o CMakeFiles/create.dir/src/packet.cpp.s

CMakeFiles/create.dir/src/types.cpp.o: CMakeFiles/create.dir/flags.make
CMakeFiles/create.dir/src/types.cpp.o: /home/raspberrypi/libcreate/src/types.cpp
CMakeFiles/create.dir/src/types.cpp.o: CMakeFiles/create.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object CMakeFiles/create.dir/src/types.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/create.dir/src/types.cpp.o -MF CMakeFiles/create.dir/src/types.cpp.o.d -o CMakeFiles/create.dir/src/types.cpp.o -c /home/raspberrypi/libcreate/src/types.cpp

CMakeFiles/create.dir/src/types.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/create.dir/src/types.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/src/types.cpp > CMakeFiles/create.dir/src/types.cpp.i

CMakeFiles/create.dir/src/types.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/create.dir/src/types.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/src/types.cpp -o CMakeFiles/create.dir/src/types.cpp.s

# Object files for target create
create_OBJECTS = \
"CMakeFiles/create.dir/src/create.cpp.o" \
"CMakeFiles/create.dir/src/serial.cpp.o" \
"CMakeFiles/create.dir/src/serial_stream.cpp.o" \
"CMakeFiles/create.dir/src/serial_query.cpp.o" \
"CMakeFiles/create.dir/src/data.cpp.o" \
"CMakeFiles/create.dir/src/packet.cpp.o" \
"CMakeFiles/create.dir/src/types.cpp.o"

# External object files for target create
create_EXTERNAL_OBJECTS =

libcreate.so: CMakeFiles/create.dir/src/create.cpp.o
libcreate.so: CMakeFiles/create.dir/src/serial.cpp.o
libcreate.so: CMakeFiles/create.dir/src/serial_stream.cpp.o
libcreate.so: CMakeFiles/create.dir/src/serial_query.cpp.o
libcreate.so: CMakeFiles/create.dir/src/data.cpp.o
libcreate.so: CMakeFiles/create.dir/src/packet.cpp.o
libcreate.so: CMakeFiles/create.dir/src/types.cpp.o
libcreate.so: CMakeFiles/create.dir/build.make
libcreate.so: /usr/lib/aarch64-linux-gnu/libboost_system.so.1.74.0
libcreate.so: /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.74.0
libcreate.so: /usr/lib/aarch64-linux-gnu/libboost_atomic.so.1.74.0
libcreate.so: CMakeFiles/create.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Linking CXX shared library libcreate.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/create.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/create.dir/build: libcreate.so
.PHONY : CMakeFiles/create.dir/build

CMakeFiles/create.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/create.dir/cmake_clean.cmake
.PHONY : CMakeFiles/create.dir/clean

CMakeFiles/create.dir/depend:
	cd /home/raspberrypi/libcreate/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/raspberrypi/libcreate /home/raspberrypi/libcreate /home/raspberrypi/libcreate/build /home/raspberrypi/libcreate/build /home/raspberrypi/libcreate/build/CMakeFiles/create.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/create.dir/depend

