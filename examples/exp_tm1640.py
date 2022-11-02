import tm1640
from machine import Pin

tm = tm1640.TM1640(clk=Pin(2), dio=Pin(4))

tm.write([
    0b00000000,
    0b01100110,
    0b01100110,
    0b00000000,
    0b00000000,
    0b10000001,
    0b01111110,
    0b00000000,
])