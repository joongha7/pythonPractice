import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)    # set board mode to Broadcom

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

colors = { 'red':(1, 0, 0), 'green':(0, 1, 0), 'blue':(0, 0, 1) }

while True:
    GPIO.output(3,0)
    GPIO.output(5,0)
    GPIO.output(7,0)
    
    color = input('color? ')    
    if color in colors:
        if color == "red":
            GPIO.output(3, colors('red')[0])
        elif color == "green":
            GPIO.output(5, colors('green')[1])
        elif color == "blue":
            GPIO.output(7, colors('blue')[2])
    else:
        print('Unknown color')
    time.sleep(0.6)

GPIO.cleanup
