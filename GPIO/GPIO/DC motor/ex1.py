import RPi.GPIO as GPIO
import time

in1=14
in2=15
ena=4

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
#GPIO.setup(ena, GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
while True:
    inp=input()
    if inp=="w":
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    if inp=="s":
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
    if inp=="y":
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.HIGH)
    if inp=="stop":
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

GPIO.cleanup()