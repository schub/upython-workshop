# It's nice have you here at the workshop! (Theatermaschine by Markus Schubert and Georg Werner)

from machine import Pin
from time import sleep



class Steppermotor:
    def __init__(self, in1, in2, in3, in4):
        IN1 = Pin(in1,Pin.OUT)
        IN2 = Pin(in2,Pin.OUT)
        IN3 = Pin(in3,Pin.OUT)
        IN4 = Pin(in4,Pin.OUT)
        self.step = 0
        self.pins = [IN1, IN2, IN3, IN4]
        self.sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

    def turn(self, steps):
        if steps > 0:
            richtung = -1
        elif steps < 0:
            richtung = 1
            steps = steps * -1
        for _ in range(steps):
            if richtung > 0:
                self.step = self.step + 1
            elif richtung < 0:
                self.step = self.step - 1
            for i in range(4):
                self.pins[i].value(self.sequence[self.step % 4][i])
                sleep(0.001)
    
    def turn_speed(self, steps, speed):
        if steps > 0:
            richtung = -1
        elif steps < 0:
            richtung = 1
            steps = steps * -1
        for _ in range(steps):
            if richtung > 0:
                self.step = self.step + 1
            elif richtung < 0:
                self.step = self.step - 1
            for i in range(4):
                self.pins[i].value(self.sequence[self.step % 4][i])
                sleep(1/speed)
