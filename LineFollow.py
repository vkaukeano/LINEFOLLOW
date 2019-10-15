import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
# For Line Following
LOGGER = 1
Lpin = 3
Rpin = 5
GPIO.setup(Lpin, GPIO.IN)
GPIO.setup(Rpin, GPIO.IN)

# For PWM
RW_PIN = 18
LW_PIN = 13
RW_ENA = 16
LW_ENA = 11

try:
    GPIO.setwarnings(False)
    GPIO.setup(RW_PIN, GPIO.OUT)  # Right Wheel
    GPIO.setup(RW_ENA, GPIO.OUT)  # Right Wheel
    GPIO.output(RW_ENA, 1)
    GPIO.setup(LW_PIN, GPIO.OUT)  # Left Wheel
    GPIO.setup(LW_ENA, GPIO.OUT)  # Left Wheel
    GPIO.output(LW_ENA, 1)

    # initialize PWM
    r = GPIO.PWM(RW_PIN, 50)  # Arguments are pin and frequency
    r.start(0)  # Argument is initial duty cycle, it should be 0
    l = GPIO.PWM(LW_PIN, 50)  # Arguments are pin and frequency
    l.start(0)  # Argument is initial duty cycle, it should be 0

    while True:
        if (GPIO.input(Lpin) == True):
            print('STOP LEFT WHEEL!!!')
            r.ChangeDutyCycle(0)
            # time.sleep(.25)
        else:
            #print('0 Left')
            r.ChangeDutyCycle(20)

        if (GPIO.input(Rpin) == True):
            print('STOP RIGHT WHEEL!!!')
            l.ChangeDutyCycle(0)
            # time.sleep(.25)
        else:
            #print('0 Right')
            l.ChangeDutyCycle(20)  # Change duty cycle for right wheel
except:
    KeyboardInterrupt

finally:
    GPIO.cleanup()
