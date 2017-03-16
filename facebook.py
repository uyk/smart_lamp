#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# facebook.py
#
#   
 
# Import the modules used in the script
import sys
import RPi.GPIO as GPIO

# Set GPIO to Broadcom system and set RGB Pin numbers
GPIO.setmode(GPIO.BCM)
red = 17
green = 18
blue = 27

#Color - facebook
R = 78
G = 67
B = 20

# Set pins to output mode
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
 
Freq = 100 #Hz

# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

# Color brightness range is 0-100%
RED.ChangeDutyCycle(R)
GREEN.ChangeDutyCycle(G)
BLUE.ChangeDutyCycle(B)
