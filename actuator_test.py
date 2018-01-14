from ActuatorDriver import ActuatorDriver
import RPi.GPIO as GPIO
 
PIN_IN1 = 13
PIN_IN2 = 19
PIN_ENABLE = 26
actuator = ActuatorDriver(PIN_IN1, PIN_IN2, PIN_ENABLE)

assert GPIO.input(actuator._pin_in1 )
assert not GPIO.input(actuator._pin_in2)
assert not GPIO.input(actuator._pin_enable )

actuator.enable = 1

assert GPIO.input(actuator._pin_in1 )
assert not GPIO.input(actuator._pin_in2)
assert GPIO.input(actuator._pin_enable )

actuator.enable = 0

assert GPIO.input(actuator._pin_in1 )
assert not GPIO.input(actuator._pin_in2)
assert not GPIO.input(actuator._pin_enable )

actuator.direction = -1

assert not GPIO.input(actuator._pin_in1 )
assert GPIO.input(actuator._pin_in2)
assert not GPIO.input(actuator._pin_enable )

actuator.enable = 1

assert not GPIO.input(actuator._pin_in1 )
assert GPIO.input(actuator._pin_in2)
assert GPIO.input(actuator._pin_enable )

actuator.enable = 0

assert not GPIO.input(actuator._pin_in1 )
assert GPIO.input(actuator._pin_in2)
assert not GPIO.input(actuator._pin_enable )

print("Tests passed.")

GPIO.cleanup()
