import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=2
echo=13
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

while True:
    GPIO.output(TRIG,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    while GPIO.input(echo)==0:
        start=time.time()
    while GPIO.input(echo)==1:
        end=time.time()
    duration=end-start
    distance=duration*(34300/2)
    print("distance:",distance,"cm")
    time.sleep(2)
       