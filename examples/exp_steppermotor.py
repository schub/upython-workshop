from steppermotor import Steppermotor
from time import sleep

motor = Steppermotor(0,1,2,3)

motor.turn_speed(100,100)
sleep(5)
motor.turn(-100)