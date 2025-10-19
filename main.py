#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import random

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

obstacle_sensor= UltrasonicSensor(Port.S3)

color_sensor = ColorSensor(Port.S4)


def turn_to(side):
    if side == 'r':
        robot.turn(90)
        robot.straight(400)
        robot.turn(-90)
    else:
        robot.turn(-90)
        robot.straight(400)
        robot.turn(90)
    drive_ahead()

def drive_ahead():
    sides = ['r', 'l']
    turn = random.choice(sides)
    cor = color_sensor.color()
    while cor != Color.WHITE or color_sensor.reflection() < 60:
        if cor != Color.WHITE or color_sensor.reflection() < 60:
            break
        cor = color_sensor.color()
        robot.drive(125, 0)
        if obstacle_sensor.distance() < 200:
            if turn == 'r':
                turn_to('l')
            else:
                turn_to('r')
                      
drive_ahead()