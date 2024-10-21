import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # important to mention pulupdown
    
p1 = GPIO.PWM(14,10)
p2 = GPIO.PWM(15,10)
p3 = GPIO.PWM(18,10)


p1.start(40)
p2.start(40)
p3.start(40)


while True:
    
    if GPIO.input(21)==0:
        p.ChangeFrequency(15)
        
