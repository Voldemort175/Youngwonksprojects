import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
    #create PWM function with GPIO pin and frequency
    #p = GPIO.PWM(GPIO_pin,frequency)


        #start PWM with 50% duty cycle
for i in range(0,5):
    p = GPIO.PWM(14,5)
    p.start(5)
        
    time.sleep(0.5)
        #stop PWM function
    p.stop()
    time.sleep(0.5)
    
#clean the GPIO pins
GPIO.cleanup() 
