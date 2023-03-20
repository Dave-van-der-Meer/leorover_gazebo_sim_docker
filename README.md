# Leo Sim Docker

Leo Rover simulation using Gazebo Garden with ROS 2 Humble in a Docker container

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
Use the script `docker_run.sh` script to run the image as a container:

```shell-session
$ bash docker_run.sh
```

## Roadmap
The goal is to make this work in an simulated (and simplified) lunar environment as standalone Gazebo simulation that interfaces with ROS 2 Humble. The idea is to use this as a baseline for SLAM and navigation tasks for educational purposes.

## License
MIT license.

## Project status
First version can be considered ready. Some cleaning up might be necessary and the rover is not turning very well. Needs some tuning. Suggestions are welcome.
