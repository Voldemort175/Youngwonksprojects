import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pinl=14
pinb=21

GPIO.setup(pinl, GPIO.OUT)
GPIO.setup(pinb, GPIO.IN)
while True:
    GPIO.output(pinl,not GPIO.input(pinb))
    time.sleep(0.2)
#     GPIO.output(pin_number,GPIO.LOW)
#     time.sleep(1)
GPIO.cleanup()
    