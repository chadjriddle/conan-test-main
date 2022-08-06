cmake_minimum_required(VERSION 3.10)

# set the project name
project(ConanTestMain VERSION 1.0)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

#include(CTest)

# setup Conan
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup() 

# add source
add_subdirectory(src)

# add tests
#add_subdirectory(tests)

