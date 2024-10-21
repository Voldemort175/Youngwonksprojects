import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pinl=14
pinb=21
pinb2=20

cnt=0
cnt2=0

GPIO.setup(pinl, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinb, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinb2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:    
    if GPIO.input(pinb)==0:
        time.sleep(1)
        cnt+=1
    if GPIO.input(pinb2)==0:  
        time.sleep(1)
        cnt2+=1
    if cnt==2 and cnt2==1:
        for i in range(0,10):
                    GPIO.output(pinl,GPIO.HIGH)
                    time.sleep(0.2)
                    GPIO.output(pinl,GPIO.LOW)
                    time.sleep(0.2)
        cnt,cnt2=0,0
GPIO.cleanup()


