import RPi.GPIO as GPIO
import time
import getch
import pygame
import random
import time
import math
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")

in1=14
in2=15
ena=4
enb=25
in4=23
in3=24

ir=19

GPIO.setmode(GPIO.BCM)

TRIG=2
echo=13
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)

GPIO.setup(ir, GPIO.IN)

p1=GPIO.PWM(ena,15)
p2=GPIO.PWM(enb,15)
p1.start(50)
p2.start(50)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

inp="k"
while True:
   
       
    if GPIO.input(ir)==0:
        print("OBJECT")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        time.sleep(0.1)
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
    else:
        print("no object")
        time.sleep(0.1)
        print("inp=",inp)
        if inp=="w":
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            
        if inp=="s":
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
           
        if inp=="a":
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            
        if inp=="d":
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            
        if inp=="b":
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
    pygame.display.update()
    for event in pygame.event.get():
        print("for")
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                inp="w"
            if event.key == K_s:
                inp="s"
            if event.key == K_a:
                inp="a"
            if event.key == K_d:   
                inp="d"
            if event.key == K_b:   
                inp="b"
GPIO.cleanup()