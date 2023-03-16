# Leo Sim Docker

Leo Rover simulation using Gazebo Garden with ROS 2 Humble in a Docker container

## Description
This repository contains the files to run a simulation of the Leo Rover using Gazebo Garden with ROS 2 Humble. Since there is no official ROS 2 simulation for the Leo ROver, this repository has been developed. It uses Docker since it makes it easy to run the simulation in any Linux based operating system. Also, it makes it easier to handle the Gazebo simulation, which is a bit more difficult to handle since the latest changes concerning Gazebo and Ignition Gazebo.

## Installation
You need to have Docker installed.

## Usage
Use the script `docker_build.sh` to build the Dockerfile and the `docker_run.sh` script to run the image as a container.

## Roadmap
The goal is to make this work in an empty world as standalone Gazebo simulation. Next, integrate it with ROS 2 Humble. Lastly, we need to add some basic worlds for the rover to interact with and drive around.

## License
I opt for an MIT license.

## Project status
Slow but making progress. Not production ready yet.
