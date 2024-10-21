import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

controlpin=[14,15,18,2]

for pin in controlpin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    
seq=[[1,0,0,0],
     [1,1,0,0],
     [0,1,0,0],
     [0,1,1,0],
     [0,0,1,0],
     [0,0,1,1],
     [0,0,0,1],
     [1,0,0,1]]

for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(controlpin[pin], seq[halfstep][pin])
        time.sleep(0.001)
GPIO.cleanup()     