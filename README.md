# Leo Sim Docker

Leo Rover simulation using Gazebo Garden with ROS 2 Humble in a Docker container

![Screenshot of the simulation](thumbnail.png)

## Description
This repository contains the files to run a simulation of the Leo Rover using Gazebo Garden with ROS 2 Humble. Since there is no official ROS 2 simulation for the Leo ROver, this repository has been developed. It uses Docker since it makes it easy to run the simulation in any Linux based operating system. Also, it makes it easier to handle the Gazebo simulation, which is a bit more difficult to handle since the latest changes concerning Gazebo and Ignition Gazebo.

## Installation
You need to have Docker installed. If this is not the case, follow the instruction from the [Docker installation page for Ubuntu](https://docs.docker.com/engine/install/ubuntu/) or use the convenience installation scripts provided by Docker:

```shell-session
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```

After this, you may want to set up the environment so that you don't need to be superuser to run Docker:

```shell-session
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
```

Then, clone this repository:

```shell-session
$ git clone https://github.com/Dave-van-der-Meer/leorover_gazebo_sim_docker.git
$ cd leorover_gazebo_sim_docker
```

Then, build the Docker image using the script called `docker_build.sh`:

```shell-session
$ bash docker_build.sh
```

## Usage
Use the script `docker_run.sh` script to run the image as a container. To run it, you need to be at the main directory of the repository, not inside the `docker` directory as otherwise the relative path to the `ros2_ws` will not be found properly:

```shell-session
$ bash docker/docker_run.sh
```
## Debugging if the host cannot see the topics

It might happen that the host system is not seeing the topics published and subscribed to by the Gazebo bridge. The docker environment has been set up to use the same `ROS_DOMAIN_ID` as the host system. If the host system has no `ROS_DOMAIN_ID` defined, this value cannot be copied into the docker environment and as a result, the topics cannot be seen by the host.

If the `ROS_DOMAIN_ID` has been defined properly on the host system, and the topics are still not visible when the docker simulation is running, you might have to modify the DDS profile. For this, create a file inside your home directory inside the `.ros/` directory:

```shell-session
$ gedit ~/.ros/fastdds.xml
```

Then, add the following xml configuration into this `fastdds.xml` file and save it.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<profiles xmlns="http://www.eprosima.com/XMLSchemas/fastRTPS_Profiles">
    <transport_descriptors>
        <transport_descriptor>
            <transport_id>UdpTransport</transport_id>
            <type>UDPv4</type>
        </transport_descriptor>
    </transport_descriptors>

    <participant profile_name="udp_transport_profile" is_default_profile="true">
        <rtps>
            <userTransports>
                <transport_id>UdpTransport</transport_id>
            </userTransports>
            <useBuiltinTransports>false</useBuiltinTransports>
        </rtps>
    </participant>
</profiles>
```

Next, add the following line to your `.bashrc` file:

```shell
export FASTRTPS_DEFAULT_PROFILES_FILE=~/.ros/fastdds.xml
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
```

With these configurations, the topics should be visible on the host system.



## Roadmap
The goal is to make this work in an simulated (and simplified) lunar environment as standalone Gazebo simulation that interfaces with ROS 2 Humble. The idea is to use this as a baseline for SLAM and navigation tasks for educational purposes.

## License
MIT license.

## Project status
First version can be considered ready. Some cleaning up might be necessary and the rover is not turning very well. Needs some tuning. Suggestions are welcome.
