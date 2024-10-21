import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pins=[2,3,4,14,6,13,19,26]

for i in pins:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
chars=[[0,1,1,1,1,1,1,1],
       [0,0,0,1,1,0,0,0],
       [1,0,1,1,0,1,1,1],
       [1,0,1,1,1,1,0,1],
       [1,1,0,1,1,0,0,1],
       [1,1,1,0,1,1,1,1],
       [0,0,1,1,1,0,0,0],
       [1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,0,1]
       ]

while True:
    for i in range(len(chars)):
        for j in range(len(pins)):
            GPIO.output(pins[j],chars[i][j])
        time.sleep(1)
GPIO.cleanup()
       