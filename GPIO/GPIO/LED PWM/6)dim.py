import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

p = GPIO.PWM(14,10)
p2= GPIO.PWM(15,10)
j=100
for i in range(0,100,5):
    p.start(i)
    p2.start(j)
    time.sleep(0.2)
    p.stop()
    p2.stop()
    time.sleep(0.2)
    j-=5
j=0
for i in range(100,-1,-5):
    #create PWM function with GPIO pin and frequency
    #p = GPIO.PWM(GPIO_pin,frequency)
    p.start(i)
    p2.start(j)
    time.sleep(0.2)
    
    #stop PWM function
    p.stop()
    p2.stop()
    time.sleep(0.2)
    j+=5
#clean the GPIO pins
GPIO.cleanup()
