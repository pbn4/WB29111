import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class ActuatorDriver(object):

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if value == 1 or value == -1:
            self._direction = value
            if value == 1:
                GPIO.output(self._pin_in1, 1)
                GPIO.output(self._pin_in2, 0)
            else:
                GPIO.output(self._pin_in1, 0)
                GPIO.output(self._pin_in2, 1)
        else:
            raise ValueError("Direction must be -1 or 1")

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        if value == 1 or value == 0:
            self._enable = value
            GPIO.output(self._pin_enable, value) 
        else:
            raise ValueError("Enable must be 0 or 1")

    def __init__(self, pin_in1, pin_in2, pin_enable):
        self._pin_in1 = pin_in1
        self._pin_in2 = pin_in2
        self._pin_enable = pin_enable
        GPIO.setup(self._pin_in1, GPIO.OUT) 
        GPIO.setup(self._pin_in2, GPIO.OUT)
        GPIO.setup(self._pin_enable, GPIO.OUT)
        self.enable = 0
        self.direction = 1
        self.speed = 1


