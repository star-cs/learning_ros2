cmake_minimum_required(VERSION 3.8)

project(ros2_cpp)

find_package(rclcpp REQUIRED)
include_directories(${rclcpp_INCLUDE_DIRS})

add_executable(00_first_node ./00_first_node.cc)
target_link_libraries(00_first_node ${rclcpp_LIBRARIES})