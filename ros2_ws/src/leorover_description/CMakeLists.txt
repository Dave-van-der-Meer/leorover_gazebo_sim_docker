cmake_minimum_required(VERSION 3.5)
project(leorover_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY
    config
    launch
    models
    urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
