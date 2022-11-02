import tm1637
from machine import Pin
seg = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

# show "12:59"
seg.numbers(12, 59)

# show "COOL"
#seg.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])

# all LEDS on "88:88"
#seg.write([127, 255, 127, 127])