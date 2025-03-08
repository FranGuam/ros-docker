FROM osrf/ros:noetic-desktop-full

# Update all packages
RUN apt update && apt upgrade -y

# Install Git
RUN apt install -y git

# Create Symlinks for Python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Python3-pip
RUN apt install -y python3-pip

# Configure pip source for Mainland China users
RUN pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
