import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin_number=[14,18,23,25,7]
for i in pin_number:
    GPIO.setup(pin_number, GPIO.OUT)
    
print("Enter username")

user=input()
if user=="admin":
    print("Enter password")
    pswd=input()
    if pswd=="haha":
        GPIO.output(23,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(23,GPIO.LOW)
    else:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(25,GPIO.LOW)
        
else:
    GPIO.output(14,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(14,GPIO.LOW)
    
GPIO.cleanup()