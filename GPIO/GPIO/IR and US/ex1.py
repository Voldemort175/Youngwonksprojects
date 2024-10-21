import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)

while True:
    if GPIO.input(19)==0:
        print("OBJECT")
        time.sleep(0.1)
    else:
        print("no object")
        time.sleep(0.1)