import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(11, 0)
GPIO.output(13, 0)

time.sleep(1)

red = GPIO.PWM(11, 100)
green = GPIO.PWM(13, 100)

red.start(0)
green.start(100)
for i in range(100):
    red.start(i)
    green.start(100-i)
    time.sleep(4)
    
for i in range(100):
    red.start(100-i)
    green.start(i)
    time.sleep(0.1)
