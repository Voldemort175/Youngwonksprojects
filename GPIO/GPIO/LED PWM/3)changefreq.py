import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
    #create PWM function with GPIO pin and frequency
    #p = GPIO.PWM(GPIO_pin,frequency)


        #start PWM with 50% duty cycle
p = GPIO.PWM(14,2)
for j in range(0,10):
    for i in range(0,10):
        p.start(50)
        p.ChangeFrequency(3)   
        time.sleep(0.1)
            #stop PWM function
    
GPIO.cleanup() 

