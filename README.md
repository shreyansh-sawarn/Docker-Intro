# Docker-Intro

Learn to build and deploy your distributed applications easily with Docker 🐳.

# Overview

[Docker](https://www.docker.com/) is an open-source project that automates the deployment of software applications inside containers by providing an additional layer of abstraction and automation of OS-level virtualization on Linux. 
In simpler words, Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources.

What are containers?

The industry standard today is to use Virtual Machines (VMs) to run software applications. VMs run applications inside a guest Operating System, which runs on virtual hardware powered by the server’s host OS.
VMs are great at providing full process isolation for applications: there are very few ways a problem in the host operating system can affect the software running in the guest operating system, and vice-versa. But this isolation comes at great cost — the computational overhead spent virtualizing hardware for a guest OS to use is substantial.
Containers take a different approach: by leveraging the low-level mechanics of the host operating system, containers provide most of the isolation of virtual machines at a fraction of the computing power.

Why use containers?

Containers offer a logical packaging mechanism in which applications can be abstracted from the environment in which they actually run. This decoupling allows container-based applications to be deployed easily and consistently, regardless of whether the target environment is a private data center, the public cloud, or even a developer’s personal laptop. This gives developers the ability to create predictable environments that are isolated from the rest of the applications and can be run anywhere.
From an operations standpoint, apart from portability containers also give more granular control over resources giving your infrastructure improved efficiency which can result in better utilization of your compute resources.
Containers sit on top of a physical server and its host OS — typically Linux or Windows. Each container shares the host OS kernel and, usually, the binaries and libraries, too. Shared components are read-only. Sharing OS resources such as libraries significantly reduces the need to reproduce the operating system code, and means that a server can run multiple workloads with a single operating system installation. Containers are thus exceptionally light — they are only megabytes in size and take just seconds to start. Compared to containers, VMs take minutes to run and are an order of magnitude larger than an equivalent container.

# Setup

Instructions to install Docker:

[Install Docker Desktop](https://docs.docker.com/install/)

To not run `sudo` everytime you run a Docker command, give it group access (for linux based systems):

    sudo groupadd docker
    sudo gpasswd -a $USER docker
    newgrp docker # or logout to apply changes

# Docker Basics

You can run Ubuntu 20.04 with the following Docker command:

    docker container run -it --rm ubuntu:20.04 bash

The `-it` gives an interactive terminal (kind of like SSH'ing into the container), and  `--rm` removes the container after you leave the container. `ubuntu:20.04` is the docker image that you will pull from [Docker Hub](https://hub.docker.com/), a collection of Docker images.  In this `ubuntu` is the Docker repository and `20.04` is the tag.  You could also do `18.04` or any other version of Ubuntu that there is a tag for (see [here](https://hub.docker.com/_/ubuntu?tab=tags)).

[Here](https://github.com/wsargent/docker-cheat-sheet) is an excellent and more complete reference.

# Dockerfile

A Dockerfile (named, `Dockerfile`, with no extension, by default) is something that specifies how to build a Docker image.  Each line in a Dockerfile has a command/instruction like `FROM`, `RUN`, `CMD`, `COPY`, etc. and creates new context. The Docker daemon runs the commands/instructions in the Dockerfile one-by-one, committing the result of each instruction to a new image if necessary, before finally outputting the ID of your new image. The Docker daemon will automatically clean up the context you sent. A context can be thought of as an intermediate Docker image (like a class, not an instance), and you build your Docker image, which makes Docker containers (the instance), by adding one or more contexts on existing Docker images (like Ubuntu).

P.S. - Docker uses a caching system when building containers, making it so that each line in a Dockerfile is saved. This means that running a Dockerfile the second time is almost instant. It also means that when writing you're Dockerfile, try not to change lines that are at the top of the file because it will have to rebuild everything below it.

A few important points:

- Don't use `sudo` because running a Dockerfile creates an image with super user permissions by default. If you want to run commands as a user in the Dockerfile and to use `sudo`, you will have to install it with `apt install sudo` first and configure it accordingly.
- A Dockerfile must not require user input in any commands/instructions during build because if they do, the Dockerfile will fail to build. Instead, automatically accept(input -yes/y in command), for example `apt install -y curl`.
- It is good practice to make several installs at once (and even several statements) to save build time. You can use `\` to continue on a new line and `&&` to run another command after the last one succeeds. For example:

        RUN apt update && apt upgrade -y \
        	&& apt install -y \
        		curl \
        		wget \
        		tmux \
        	&& rm -rf /var/lib/apt/lists/* # best practice to remove apt install stuff

Here is a minimal example:

    # Saved as `Dockerfile`
    FROM ubuntu:20.04

    RUN apt update && apt upgrade -y \
    	&& apt install -y \
    		curl \
    		wget \
    		tmux \
    	&& rm -rf /var/lib/apt/lists/* # best practice to remove apt install stuff

    CMD ["bash"]

From command line:

    cd <directory/with/the/dockerfile>

    # Build the docker image from the Dockerfile
    docker build . -t example

    # See that the image called example:latest has been created
    docker image list

    # Run the created image
    docker run -it example
    
    # Note that we do not need to call bash to run bash as it was set to run with CMD in the Dockerfile
    # Also, latest is the default tag if you don't specify whenever you pull a docker image from docker hub

# Docker-Compose

Compose is a tool for defining and running multi-container Docker applications. With compose, you use a YAML file to configure your application's services. With a single command, you create and start all the services from your configuration. Run docker-compose up and compose starts and runs your entire app.

Using Compose is basically a three-step process:

    Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
    
    Define the services that make up your app in docker-compose.yml so that they can be run together in an isolated environment.
    
    Run docker-compose up and Compose starts and runs your entire app.

# Sample Docker Applications

To run the Flask Docker app using Dockerfile, follow the instructions [here](https://github.com/shreyansh-sawarn/Docker-Intro/blob/main/flask-app/README.md).

To run the Apache-PHP Docker app using docker-compose, follow the instructions [here](https://github.com/shreyansh-sawarn/Docker-Intro/blob/main/apache-php-app/README.md).
