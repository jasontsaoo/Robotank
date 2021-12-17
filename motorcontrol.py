Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pygame
import time,sys
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)

GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

def init():
    pygame.init()
    win=pygame.display.set_mode((100,100))
    
def getKey(keyName):
    ans=False
    for eve in pygame.event.get():pass
    keyInput=pygame.key.get_pressed()
    myKey=getattr(pygame,'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans=True
    pygame.display.update()
    return ans

while True:  
    init()


    if getKey('w'):
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        time.sleep(0.25)
            
    elif getKey('s'):
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        time.sleep(0.25)
        
    elif getKey('a'):
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        time.sleep(0.25)
        
    elif getKey('d'):
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        time.sleep(0.25)
        
    elif getKey('q'):
        GPIO.output(16,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        pygame.quit()
        exit()


    else:
        GPIO.output(16,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)