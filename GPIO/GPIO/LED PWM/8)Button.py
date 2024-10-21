import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
p = GPIO.PWM(14,10)
cnt=1
p.start(10)

while True:
    
    if GPIO.input(21)==0:
        time.sleep(1)
        cnt+=1
        print("pressed")
    if cnt % 2 == 0:    
        p.ChangeDutyCycle(80)
        
    else:
        p.ChangeDutyCycle(10)
        