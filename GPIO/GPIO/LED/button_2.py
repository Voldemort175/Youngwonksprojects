import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pinl=14
pinb=21

GPIO.setup(pinl, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinb, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    
    while GPIO.input(pinb)==0:
            GPIO.output(pinl,GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(pinl,GPIO.LOW)
            time.sleep(0.2)
    else:
        GPIO.output(pinl,GPIO.LOW)
#     time.sleep(1)
GPIO.cleanup()