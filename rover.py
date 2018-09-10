from motor import Motor
import wiringpi
import time
from ultrasonic import DistanceMeasurer

MAX_SPEED = 480
class Rover(object):

    def __init__(self):

        
        #Motor pins 
        pwm_pin_1 = 12
        pwm_pin_2 = 13

        dir_pin_1 = 24 
        dir_pin_2 = 25

        en_pin_1 = 22
        en_pin_2 = 23

        #Ultrasonic sensor
        trigger_pin = 8
        echo_pin = 7

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(pwm_pin_1, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pinMode(pwm_pin_2, wiringpi.GPIO.PWM_OUTPUT)

        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        wiringpi.pwmSetRange(MAX_SPEED)
        wiringpi.pwmSetClock(2)

        wiringpi.pinMode(en_pin_1, wiringpi.GPIO.OUTPUT)
        wiringpi.pinMode(en_pin_2, wiringpi.GPIO.OUTPUT)
        wiringpi.pinMode(dir_pin_1, wiringpi.GPIO.OUTPUT)
        wiringpi.pinMode(dir_pin_2, wiringpi.GPIO.OUTPUT)

        self.motor_left = Motor(pwm_pin_1, dir_pin_1, en_pin_1)
        self.motor_right = Motor(pwm_pin_2, dir_pin_2, en_pin_2)

        self.us = DistanceMeasurer(1, trigger_pin, echo_pin)


    #UNDER DEVELOPMENT, Just for testing purpose    
    def start(self):
        self.motor_left.enable()
        self.motor_right.enable()

    def forward(self):
        self.motor_left.setSpeed(100)
        time.sleep(1)
        self.motor_left.setSpeed(0)


rover = Rover()
rover.start()
rover.forward()