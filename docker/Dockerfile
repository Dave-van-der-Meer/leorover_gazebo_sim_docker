# Use the official ROS2 image as the base image
FROM ros:humble-ros-base
LABEL maintainer="Dave van der Meer <dave.vandermeer@uni.lu>"
ENV ROS_VERSION "humble"
ENV GZ_VERSION "garden"

RUN useradd -ms /bin/bash leo

# Install ROS2 packages
RUN apt update && \
    apt install -y \
    lsb-release \
    wget \
    gnupg\
    ros-$ROS_VERSION-gazebo-ros \
    vim

# Install Gazebo Garden (binary install: https://gazebosim.org/docs/garden/install_ubuntu)
RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
RUN apt update && \
    apt install -y gz-garden \
    ros-cmake-modules \
    libgflags-dev \
    ros-$ROS_VERSION-gps-msgs \
    ros-$ROS_VERSION-image-transport \
    ros-$ROS_VERSION-xacro \
    ros-$ROS_VERSION-rviz2 \
    ros-$ROS_VERSION-actuator-msgs \
    ros-$ROS_VERSION-vision-msgs \
    python3-pip && \
    pip install setuptools==58.2.0

# Clean up apt package list
RUN rm -rf /var/lib/apt/lists/*

# Set up entrypoint to source ROS2 setup files
COPY ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

USER leo
WORKDIR /home/leo

RUN mkdir -p /home/leo/ros2_ws/src/
WORKDIR /home/leo/ros2_ws/src/
RUN git clone -b $ROS_VERSION --single-branch https://github.com/gazebosim/ros_gz.git
RUN git clone -b humble --single-branch https://github.com/ros/sdformat_urdf.git
WORKDIR /home/leo/ros2_ws/
RUN /bin/bash -c "source /opt/ros/humble/setup.bash; colcon build --symlink-install --executor sequential"

# COPY gazebo_leorover_model/ /home/leo/gazebo_leorover_model/

# Set the default command to run when the container starts
CMD ["bash"]
