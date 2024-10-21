import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin_number=[14,18,23,25,7]
for i in pin_number:
    GPIO.setup(pin_number, GPIO.OUT)

for i in range(0,len(pin_number)):
    GPIO.output(pin_number[i],GPIO.HIGH)
    time.sleep(2)
    
    
for i in range(len(pin_number)-1,-1,-1):
    GPIO.output(pin_number[i],GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()
