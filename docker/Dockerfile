# Use the official ROS2 image as the base image
FROM ros:humble-ros-base
LABEL maintainer="Dave van der Meer <dave.vandermeer@uni.lu>"
ENV ROS_VERSION "humble"
# ENV GZ_VERSION "classic"

RUN useradd -ms /bin/bash leo

# Install ROS2 packages
RUN apt update && \
    apt install -y \
    lsb-release \
    wget \
    gnupg\
    ros-$ROS_VERSION-gps-msgs \
    ros-$ROS_VERSION-image-transport \
    ros-$ROS_VERSION-gazebo-ros \
    ros-$ROS_VERSION-xacro \
    ros-$ROS_VERSION-controller-manager \
    vim
RUN apt install -y python3-pip && pip install setuptools==58.2.0


# Clean up apt package list
RUN rm -rf /var/lib/apt/lists/*


# Set up entrypoint to source ROS2 setup files
COPY ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

# Switch user to non-root user
USER leo
WORKDIR /home/leo

# Create ros2_ws to import ROS 2 packages as volumes here
RUN mkdir -p /home/leo/ros2_ws/src/

# Set the default command to run when the container starts
CMD ["bash"]
