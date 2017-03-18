#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# default.py
#
#   
 
# Import the modules used in the script
import sys
import RPi.GPIO as GPIO

# Set GPIO to Broadcom system and set RGB Pin numbers
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
red = 17
green = 18
blue = 27

#Color - facebook
R = 0
G = 0
B = 0

# Set pins to output mode
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
 
Freq = 100 #Hz

# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(red, Freq)
RED.start(R)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(G)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(B)

# Color brightness range is 0-100%
#RED.ChangeDutyCycle(R)
#GREEN.ChangeDutyCycle(G)
#BLUE.ChangeDutyCycle(B)

print "default.py"
