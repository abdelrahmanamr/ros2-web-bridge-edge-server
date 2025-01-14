# ROS 2 Web Bridge Edge Server

This project is particularly useful for handling incoming frames through the ROS 2 Web Bridge, processing them using the DOPE (Deep Object Pose Estimation) model, and publishing the resulting points back to the ROS 2 network.

---

## Features
- **ROS 2 Integration**: Enables communication between ROS 2 nodes and web-based applications.
- **WebSocket Support**: Uses WebSockets to facilitate real-time, bidirectional communication.
- **Cross-Platform Compatibility**: Works with devices that cannot natively run ROS 2, such as mobile phones and embedded systems.

---
## Installation

### Prerequisites
- **ROS 2 Humble**: Ensure ROS 2 is installed on your system. Follow the official [ROS 2 installation guide](https://docs.ros.org/en/humble/Installation.html).
- **ROS2-Web-Bridge**: Ensure ROS2 web bridge is installed and run on your system. Follow the official [ROS2-web-bridge installation guide](https://github.com/RobotWebTools/ros2-web-bridge).
- **mustard_60.pth**: Ensure mustard_60.pth file is downloaded in the coordinates_puplisher directory. Follow the [Deep_Object_Pose](https://github.com/NVlabs/Deep_Object_Pose).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/abdelrahmanamr/ros2-web-bridge-edge-server.git
   cd ros2-web-bridge-edge-server

2. Build and source the ROS 2 workspace:
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select coordinates_publisher
   source install/setup.bash

3. Run the package
   ```bash
   ros2 run coordinates_publisher publisher_node

---
## Demo
A demo video showcasing the functionality of this project is available on this [link](https://drive.google.com/drive/folders/1SYTTRWaFQHZBB-C2ngWCZ6FboDucJ3bx?usp=sharing).


   

