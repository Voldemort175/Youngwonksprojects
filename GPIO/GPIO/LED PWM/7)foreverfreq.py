import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
    
p = GPIO.PWM(14,10)
p.start(50)
while True:
    for i in range(10,91,10):
        p.ChangeFrequency(i)
        time.sleep(0.2)
    for i in range(90,9,-10):
        p.ChangeFrequency(i)
        time.sleep(0.2)
    
p.stop()
GPIO.cleanup() 