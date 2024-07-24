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
include CMakeFiles/test_robot_model.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/test_robot_model.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/test_robot_model.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_robot_model.dir/flags.make

CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o: CMakeFiles/test_robot_model.dir/flags.make
CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o: /home/raspberrypi/libcreate/tests/test_robot_model.cpp
CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o: CMakeFiles/test_robot_model.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o -MF CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o.d -o CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o -c /home/raspberrypi/libcreate/tests/test_robot_model.cpp

CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raspberrypi/libcreate/tests/test_robot_model.cpp > CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.i

CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raspberrypi/libcreate/tests/test_robot_model.cpp -o CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.s

# Object files for target test_robot_model
test_robot_model_OBJECTS = \
"CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o"

# External object files for target test_robot_model
test_robot_model_EXTERNAL_OBJECTS =

test_robot_model: CMakeFiles/test_robot_model.dir/tests/test_robot_model.cpp.o
test_robot_model: CMakeFiles/test_robot_model.dir/build.make
test_robot_model: libcreate.so
test_robot_model: /usr/lib/aarch64-linux-gnu/libgtest.a
test_robot_model: /usr/lib/aarch64-linux-gnu/libboost_system.so.1.74.0
test_robot_model: /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.74.0
test_robot_model: /usr/lib/aarch64-linux-gnu/libboost_atomic.so.1.74.0
test_robot_model: CMakeFiles/test_robot_model.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/raspberrypi/libcreate/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test_robot_model"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_robot_model.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_robot_model.dir/build: test_robot_model
.PHONY : CMakeFiles/test_robot_model.dir/build

CMakeFiles/test_robot_model.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_robot_model.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_robot_model.dir/clean

CMakeFiles/test_robot_model.dir/depend:
	cd /home/raspberrypi/libcreate/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/raspberrypi/libcreate /home/raspberrypi/libcreate /home/raspberrypi/libcreate/build /home/raspberrypi/libcreate/build /home/raspberrypi/libcreate/build/CMakeFiles/test_robot_model.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_robot_model.dir/depend

