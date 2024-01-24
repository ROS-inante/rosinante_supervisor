# ROSinante Supervisor

This repository contains the firmware configuration and main controller scripts for the ROSinante Supervisor module.

## Overview
The supervisor module consists of an ESP32 connected to bumper switches as well as the main and auxilary power relays and one user button.
For details on its operation, please see the thesis available in the [main project repository](https://github.com/aJunk/ROSinante).

The ESP32 runs the awesome [Tasmota](https://tasmota.github.io/docs/) firmware.
The e-Stop behaviour is implemented through the standard 'rule' functionality in Tasmota.

On the main robot controller running linux, a systemd-service connects to the ESP32 via USB. It listens for events (such as a button press) and controls the robot software stack accordingly.

The started software modules are put into separate termux sessions for ease of inspection.

## Usage
1) Make sure you have a working installation of termux, python3 and pyserial.
2) Copy the files in the [linux/opt](/linux/opt/) folder into a folder named /opt/rosinante/ on the main controller and make sure they are marked as executable.
3) At the top of the shell scripts, modify the path to your ros environment, where the robot software was built and can be sourced from.
4) At the top of [supervisor.py](/linux/opt/supervisor.py) set the path to the serial port connected to the supervisor module.
5) Add the [systemd service file](/linux/rosinante_supervisor.service) to your systemd-installation, enable it and start it.

6) Install and configure Tasmota on supervisor module (pick one):
    * Install version 12  and restore full dump from [backup](/tasmota/Config_supervisor_12.2.0.dmp).
    * (PREFERRED) Install any (newer) version and run commands from [file](/tasmota/setup.txt).

## Implemented behaviour
Start/restart the entire stack in stand-alone mode or with a motion capture node.


| Button presses |  Behaviour   |
|:-----|:--------:|:---|
| `1x` | Start in standalone mode. |
| `2x` | Start in motion-capture mode. |
| `4x` | Perform orderly shutdown of robot. |


## License
This project is licensed under the GPLv3.

