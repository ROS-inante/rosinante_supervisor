#!/usr/bin/env python3

import serial
import re
import json

import os

import multiprocessing
import subprocess

serial = serial.Serial("/dev/ttyUSB0", 115200)
serial.reset_input_buffer()

func_handler_dict = {}

def main():
    while True:
        data = serial.readline().decode("utf-8")
        print(data)
        str_list = re.findall(r'.*RESULT = ({.*})', data)

        if len(str_list) > 0:
            j = json.loads(str_list[0])
            print(j)
            handle_json(j)
        
        if 'Serial logging disabled' in data:
            serial.write("SerialLog 2\n".encode("utf-8"))

def handle_json(j):
    for key in j:
        if key in func_handler_dict:
            func_handler_dict[key](j[key])

def _handle_button4(j):
    print('Handling button 4')
    if 'Action' in j:
        action = j['Action']

        if action == 'SINGLE':
            print("Starting ROSinante controller without mocap")
            subprocess.run(['su', 'rock','-c', '/opt/rosinante/spawn_rosinante_controller.sh'])

        elif action == 'DOUBLE':
            print("Starting ROSinante controller with mocap")
            subprocess.run(['su', 'rock','-c', '/opt/rosinante/spawn_rosinante_controller_mocap.sh'])

        elif action == 'TRIPPLE':
            pass
 
        elif action == 'QUAD':
            os.system("shutdown now")
 
        elif action == 'PENTA':
            pass

func_handler_dict["Button4"] = _handle_button4


if __name__ == '__main__':
    main()
