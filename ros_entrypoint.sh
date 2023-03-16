#!/bin/bash

set -e

export ROS2_INSTALL_PATH="/opt/ros/humble"
export ROS_NAMESPACE="leo_sim"
export ROS_DOMAIN_ID=55

cd /home/leo/ros2_ws

# setup ros2 environment
source "/opt/ros/humble/setup.bash"
colcon build --symlink-install
source "/home/leo/ros2_ws/install/setup.bash"

cd /home/leo/gazebo_leorover_model

exec "$@"
