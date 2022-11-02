import config
import machine
import time
from umqttsimple import MQTTClient
import ubinascii

# button
btn = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)
counter = 0

import wifi_connect

# mqtt 
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'breakdown/schub/in'
topic_welcome = b'breakdown/taster/welcome'

def connect_and_subscribe():
    client = MQTTClient(client_id = client_id, server = config.mqtt_host, port = config.mqtt_port)
    client.connect()
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()


client.publish(topic_welcome, "hello world, I'm here now :)")


while True:
    first = btn.value()
    time.sleep(0.01)
    second = btn.value()
    if first and not second:
        counter += 1
        client.publish(topic_pub, str(counter))
