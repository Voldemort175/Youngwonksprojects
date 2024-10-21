import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
lights=[14,15,18,23,24]
for i in lights:
    GPIO.setup(i, GPIO.OUT)

GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # important to mention pullupdown
    
p1= GPIO.PWM(14,100)
p2=GPIO.PWM(15,100)
p3=GPIO.PWM(18,100)
p4=GPIO.PWM(23,100)
p5=GPIO.PWM(24,100)

pwm=[p1,p2,p3,p4,p5]
random.shuffle(pwm)
for i in pwm:
    i.start(5)

while True:
    
    if GPIO.input(21)==0:
        print("Pressed")
        for i in pwm:
            for dc in range(0,101,5):
                i.ChangeDutyCycle(dc)
                time.sleep(0.1)
        for i in range(len(pwm)-1,-1,-1):
            for dc in range(100,-1,-5):
                pwm[i].ChangeDutyCycle(dc)
                time.sleep(0.1)
                
    
        

