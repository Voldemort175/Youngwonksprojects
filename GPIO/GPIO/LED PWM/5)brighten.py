import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

p = GPIO.PWM(14,10)
for i in range(0,101,5):
    #create PWM function with GPIO pin and frequency
    #p = GPIO.PWM(GPIO_pin,frequency)
    p.start(i)
    if i==100:
        time.sleep(5)
    else:
        time.sleep(0.2)
    
    #stop PWM function
    p.stop()
    time.sleep(0.2)
#clean the GPIO pins
GPIO.cleanup()