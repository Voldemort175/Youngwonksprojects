import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin_number=14
pin_number2=12
GPIO.setup(pin_number, GPIO.OUT)
GPIO.setup(pin_number2, GPIO.OUT)
for i in range(0,5):
    GPIO.output(pin_number,GPIO.HIGH)
    GPIO.output(pin_number2,GPIO.LOW)
    time.sleep(2)
    GPIO.output(pin_number,GPIO.LOW)
    GPIO.output(pin_number2,GPIO.HIGH)  
    time.sleep(1)
GPIO.cleanup()