import machine
import time

led = machine.Pin(7, machine.Pin.OUT)
btn = machine.Pin(9, machine.Pin.IN)

while True:
    btn_pressed = btn.value()
    if (btn_pressed == 0):
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
