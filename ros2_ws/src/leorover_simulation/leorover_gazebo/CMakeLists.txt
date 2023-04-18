cmake_minimum_required(VERSION 3.5)
project(leorover_gazebo)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY
    launch
    robots
    worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
