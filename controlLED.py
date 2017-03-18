#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# controlLED.py
#
#   
 
# Import the modules used in the script
import sys, time
import RPi.GPIO as GPIO

# Set GPIO to Broadcom system and set RGB Pin numbers
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
red = 17
green = 18
blue = 27
RUN = True

#Color - facebook
R = 0
G = 0
B = 0

# Set pins to output mode
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
 
Freq = 100 #Hz



####################################### Control LED
# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

while RUN :
    line = sys.stdin.readline()
    if line :
        print "Not Empty"
        #print line
    # End roop
    if line == "END" :
        print "in END"
        #print line
        RUN = False
        break
    """
    # Parsing
    lines = lines.split(",")
    R = lines[0]
    G = lines[1]
    B = lines[2]
    # Color brightness range is 0-100%
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    """

#Close GPIO
GPIO.cleanup()
