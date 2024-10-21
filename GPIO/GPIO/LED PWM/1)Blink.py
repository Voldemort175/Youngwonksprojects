import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
for i in range(0,100,10):
    #create PWM function with GPIO pin and frequency
    #p = GPIO.PWM(GPIO_pin,frequency)
    p = GPIO.PWM(14,10)
    #start PWM with 50% duty cycle
    p.start(i)
    time.sleep(1)
    #stop PWM function
    p.stop()
    time.sleep(1)
#clean the GPIO pins
GPIO.cleanup() 