cmake_minimum_required(VERSION 3.8)
project(json_to_kml_converter)

set (CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_STANDARD_REQUIRED ON) 

find_package(PkgConfig REQUIRED)
pkg_check_modules(JSONCPP jsoncpp)
link_libraries(${JSONCPP_LIBRARIES})
add_executable(converter "converter.cpp")
target_link_libraries(converter ${JSONCPP_LIBRARIES})