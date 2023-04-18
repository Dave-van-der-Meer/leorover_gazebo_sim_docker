#!/bin/bash

set -e

export ROS2_INSTALL_PATH="/opt/ros/humble"
export IGN_GAZEBO_RESOURCE_PATH=/home/leo/ros2_ws/install/leorover_description/share:/home/leo/ros2_ws/install/ros_gz_sim_demos/share
export GZ_SIM_RESOURCE_PATH=/home/leo/ros2_ws/install/leorover_description/share:/home/leo/ros2_ws/install/ros_gz_sim_demos/share
export ROS_NAMESPACE="leo_sim"
export ROS_DOMAIN_ID=${ROS_DOMAIN_ID}

cd /home/leo/ros2_ws

# setup ros2 environment
source "/opt/ros/humble/setup.bash"
colcon build --symlink-install
source "/home/leo/ros2_ws/install/setup.bash"

cd /home/leo

exec "$@"
