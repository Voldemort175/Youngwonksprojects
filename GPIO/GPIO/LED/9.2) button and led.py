import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pinl=14
pinb=21
cnt=0

GPIO.setup(pinl, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinb, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    
    while GPIO.input(pinb)==0:
            time.sleep(1)
            cnt+=1
    if cnt%2==0:
        GPIO.output(pinl,GPIO.LOW)
    else:
        GPIO.output(pinl,GPIO.HIGH)
#     time.sleep(1)
GPIO.cleanup()