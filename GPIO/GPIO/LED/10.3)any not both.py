import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pinl=14
pinb=21
pinb2=20

GPIO.setup(pinl, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinb, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinb2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:    
    while(GPIO.input(pinb)==0 and GPIO.input(pinb2)==0):
        time.sleep(1)
        GPIO.output(pinl,GPIO.LOW)
        time.sleep(1)
    if (GPIO.input(pinb)==0 and GPIO.input(pinb2)==1):   
        time.sleep(0.2)
        GPIO.output(pinl,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pinl,GPIO.LOW)
        time.sleep(0.2)
    elif (GPIO.input(pinb)==1 and GPIO.input(pinb2)==0):   
        time.sleep(0.2)
        GPIO.output(pinl,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pinl,GPIO.LOW)
        time.sleep(0.2)
    elif (GPIO.input(pinb)==1 and GPIO.input(pinb2)==1):
        GPIO.output(pinl,GPIO.LOW)
#     time.sleep(1)
GPIO.cleanup()


