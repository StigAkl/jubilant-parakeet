import RPi.GPIO as GPIO
import time

class DistanceMeasurer(object):
    def __init__(self, interval_time, io_trigger, io_echo):
        self.trigger_pin = io_trigger
        self.echo_pin = io_echo
        self.distance = 0
        self.interval_time = interval_time
        self.run = False
        
        self.SONIC_SPEED = 34300

    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)


    def startMeasuring(self):
        self.run = True

        while self.run:
            #Set trigger to HIGH
            GPIO.output(self.trigger_pin, True)

            time.sleep(0.00001)

            GPIO.output(self.trigger_pin, False)

            startTime = 0
            endTime = 0

            while GPIO.input(self.echo_pin) == 0:
                startTime = time.time()

            while GPIO.input(self.echo_pin) == 1: 
                endTime = time.time()


            duration = endTime - startTime
            
            #Multiply duration by sonic speed (34300 cm/s) and divide by 2 (because it travels back again)
            self.distance = (duration * self.SONIC_SPEED) / 2
            print (self.getDistance(), end='\r')
            time.sleep(self.interval_time)


    def stopMeasuring(self):
        self.run = False 
        GPIO.cleanup() 
        print("Stopping..") 

    def getDistance(self):
        return self.distance