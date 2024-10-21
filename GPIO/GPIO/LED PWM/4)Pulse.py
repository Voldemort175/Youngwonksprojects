import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
    #create PWM function with GPIO pin and frequency
    #p = GPIO.PWM(GPIO_pin,frequency)


        #start PWM with 50% duty cycle
p1 = GPIO.PWM(14,50)
p2 = GPIO.PWM(15,25)
p3 = GPIO.PWM(21,16.66)
for j in range(0,10):
    time.sleep(0.8)
    p1.start(50)
    p2.start(50)
    p3.start(50)
    time.sleep(0.1)
           #stop PWM function
    p1.stop()
    p2.stop()
    p3.stop()
    time.sleep(0.1)
GPIO.cleanup() 