import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin_number=14

GPIO.setup(pin_number, GPIO.OUT)
while True:
    GPIO.output(pin_number,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(pin_number,GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()