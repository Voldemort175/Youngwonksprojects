import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pinl=14
pinl2=15
pinb=21
cnt=0

GPIO.setup(pinl, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinl2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinb, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    
    while GPIO.input(pinb)==0:
            time.sleep(1)
            cnt+=1
    if cnt==0:
        GPIO.output(pinl,GPIO.LOW)
        GPIO.output(pinl2,GPIO.LOW)
    elif cnt%2==0:
        GPIO.output(pinl,GPIO.LOW)
        GPIO.output(pinl2,GPIO.HIGH)
    else:
        GPIO.output(pinl,GPIO.HIGH)
        GPIO.output(pinl2,GPIO.LOW)
#     time.sleep(1)
GPIO.cleanup()
