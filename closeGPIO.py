#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# closeGPIO.py
#
#   
 
# Import the modules used in the script
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

red = 17
green = 18
blue = 27

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Stop and cleanup so the pins
# are available to be used again
GPIO.cleanup()
