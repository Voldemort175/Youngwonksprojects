import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin_number=14
blink=0
var=0.5
GPIO.setup(pin_number, GPIO.OUT)

while True:
    GPIO.output(pin_number,GPIO.HIGH)
    time.sleep(blink)
    GPIO.output(pin_number,GPIO.LOW)
    time.sleep(1)
    blink+=var
    if blink==2.0:
        var=-0.5
    if blink==0.5:
        var=0.5
    print(blink)
GPIO.cleanup()
