#!/bin/bash

source /opt/ros/galactic/setup.bash
source /home/rock/ros_ws/install/local_setup.bash

tmux kill-session -t ROSinante_bringup
tmux new -d -s "ROSinante_bringup" 'source /home/rock/ros_ws/install/local_setup.bash; while true; do ros2 launch rosinante_bringup rosinante.launch.py teleop_joy:=true ; done'

tmux kill-session -t ROSinante_rosbridge
tmux new -d -s "ROSinante_rosbridge" 'while true; do ros2 launch rosbridge_server rosbridge_websocket_launch.xml ; done'

tmux kill-session -t ROSinante_controller
tmux new -d -s "ROSinante_controller" 'sleep 30; while true; do ros2 run rosinante_position_controller position_controller --ros-args -p target_frame:="map" ; done'

tmux kill-session -t ROSinante_mqtt_adapter
tmux new -d -s "ROSinante_mqtt_adapter" 'while true; do ros2 run rosinante_position_controller_mqtt_adapter position_controller_mqtt_adapter_node --ros-args --remap __node:=position_controller_mqtt_adapter_node --params-file /home/rock/ros_ws/src/rosinante_bringup/config/mqtt_adapter.yaml ; done'

tmux kill-session -t ROSinante_optitrack
tmux new -d -s "ROSinante_optitrack" 'while true; do ros2 launch mocap_optitrack mocap.launch.py  ; done'
