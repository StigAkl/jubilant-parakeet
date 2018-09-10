import wiringpi 

class Motor(object):
    MAX_SPEED = 480

    def __init__(self, pwm_pin, dir_pin, en_pin):
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin 

    def enable(self):
        wiringpi.digitalWrite(self.en_pin,1)

    def disable(self):
        digitalWrite(self.en_pin, 0)
    
    def setSpeed(selv, speed):
        if speed < 0:
            speed = - speed
            dir_value = 1
        else:
            dir_value = 0
        

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        wiringpi.digitalWrite(self.dir_pin, dir_value)
        wiringpi.pwmWrite(self.pwm_pin, speed)