import config
import machine
import time
from umqttsimple import MQTTClient
import ubinascii
import wifi_connect

# mqtt 
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'breakdown/schub/in'
topic_pub = b'breakdown/schub/data'
topic_welcome = b'breakdown/schub/welcome'

def sub_cb(topic, msg):
    print("message received")
    print((topic, msg))
    print("---")

def connect_and_subscribe():
    client = MQTTClient(client_id = client_id, server = config.mqtt_host, port = config.mqtt_port)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (config.mqtt_host, topic_sub))
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
    try:
        client.check_msg()
    except OSError as e:
        restart_and_reconnect()
