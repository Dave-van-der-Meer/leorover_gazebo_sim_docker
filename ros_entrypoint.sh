#!/bin/bash

set -e

export ROS2_INSTALL_PATH="/opt/ros/humble"
export GZ_SIM_RESOURCE_PATH=/home/leo/ros2_ws/src/leorover_description:${IGN_GAZEBO_RESOURCE_PATH}
export ROS_NAMESPACE="leo_sim"
export ROS_DOMAIN_ID=${ROS_DOMAIN_ID}

cd /home/leo/ros2_ws

# setup ros2 environment
source "/opt/ros/humble/setup.bash"
colcon build --symlink-install
source "/home/leo/ros2_ws/install/setup.bash"

cd /home/leo

exec "$@"
