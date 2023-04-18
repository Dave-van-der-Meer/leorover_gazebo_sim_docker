#!/bin/bash
xhost +local:docker

## GUI
# To enable GUI, make sure processes in the container can connect to the x server
XAUTH=/tmp/.docker.xauth
if [ ! -f ${XAUTH} ]; then
    touch ${XAUTH}
    chmod a+r ${XAUTH}

    XAUTH_LIST=$(xauth nlist "${DISPLAY}")
    if [ -n "${XAUTH_LIST}" ]; then
        # shellcheck disable=SC2001
        XAUTH_LIST=$(sed -e 's/^..../ffff/' <<<"${XAUTH_LIST}")
        echo "${XAUTH_LIST}" | xauth -f ${XAUTH} nmerge -
    fi
fi

docker run \
    --interactive \
    --tty \
    --rm \
    --network host \
    --ipc host \
    --privileged \
    --env="DISPLAY" \
    --env ROS_DOMAIN_ID=${ROS_DOMAIN_ID} \
    --env IGN_GAZEBO_RESOURCE_PATH=/home/leo/ros2_ws/install/leorover_description/share:/home/leo/ros2_ws/install/ros_gz_sim_demos/share \
    --env GZ_SIM_RESOURCE_PATH=/home/leo/ros2_ws/src/leorover_description:/home/leo/ros2_ws/install/ros_gz_sim_demos/share \
    --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
    --volume ./gazebo_leorover_model:/home/leo/gazebo_leorover_model \
    --volume ./environment_models:/home/leo/environment_models \
    --volume ./ros2_ws/src/leorover_gazebo_bridge:/home/leo/ros2_ws/src/leorover_gazebo_bridge \
    --volume ./ros2_ws/src/leorover_description:/home/leo/ros2_ws/src/leorover_description \
    --device /dev/dri/renderD128:/dev/dri/renderD128 \
    --device /dev/dri/renderD129:/dev/dri/renderD129 \
    --name leo_gazebo \
    local/leo_gazebo:humble 
    # ros2 launch leorover_gazebo_bridge leorover_gazebo_sim.launch.py
    # ros2 launch leorover_gazebo_bridge ros2_control_demo.launch.py
    # --env IGN_GAZEBO_SYSTEM_PLUGIN_PATH=/home/leo/ros2_ws/install/lib${IGN_GAZEBO_SYSTEM_PLUGIN_PATH

# docker run --interactive --tty --rm --network host --ipc host --privileged --security-opt seccomp=unconfined --volume /tmp/.docker.xauth:/tmp/.docker.xauth --volume /tmp/.X11-unix:/tmp/.X11-unix --volume /dev/input:/dev/input --env XAUTHORITY=/tmp/.docker.xauth --env QT_X11_NO_MITSHM=1 --env DISPLAY=:1 --gpus all --env NVIDIA_VISIBLE_DEVICES=all --env NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics --volume /etc/localtime:/etc/localtime:ro --volume /home/dave/.ros/fastdds.xml:/home/dave/.ros/fastdds.xml:ro --env ROS_DOMAIN_ID=55 --env RMW_IMPLEMENTATION=rmw_fastrtps_cpp --env FASTRTPS_DEFAULT_PROFILES_FILE=/home/dave/.ros/fastdds.xml local/leo_gazebo:humble gz sim /home/leo/gazebo_leorover_model/leo.sdf
# docker run --privileged --security-opt seccomp=unconfined --env DISPLAY=:1  

    # --gpus all \
    # --env XAUTHORITY=/tmp/.docker.xauth \
    # --env "DISPLAY=${DISPLAY}" \
    # --env QT_X11_NO_MITSHM=1 \
    # --env NVIDIA_VISIBLE_DEVICES=all \
    # --env NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
    # --env ROS_DOMAIN_ID=55 \
    # --env RMW_IMPLEMENTATION=rmw_fastrtps_cpp \
    # --env FASTRTPS_DEFAULT_PROFILES_FILE=/home/dave/.ros/fastdds.xml \
    # --volume /tmp/.docker.xauth:/tmp/.docker.xauth \
    # --volume /tmp/.X11-unix:/tmp/.X11-unix \
    # --volume /dev/input:/dev/input \
    # --volume /etc/localtime:/etc/localtime:ro \
    # --volume /home/dave/.ros/fastdds.xml:/home/dave/.ros/fastdds.xml:ro \
    # --gpus all \