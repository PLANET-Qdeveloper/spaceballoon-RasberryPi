#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

sw_pin = 25 #撮影開始のスイッチピンにGPIO25を選択

GPIO.setup(sw_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    #撮影動作をここに書く。


