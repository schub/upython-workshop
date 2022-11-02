import config
import machine
import network
import time

led = machine.Pin(7, machine.Pin.OUT)

# connect to wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.config(txpower=8.5)
station.connect(config.wifi_ssid, config.wifi_pass)

while station.isconnected() == False:
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)
    pass

print('connected to wifi')
led.value(1)
