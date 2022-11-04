from time import sleep_us
from machine import UART, Pin
from array import array


uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1, rx=20, tx=21)


class universe():
    def __init__(self, port):
        self.port = port

        # To check if port is valid
        dmx_uart = UART(port)
        del(dmx_uart)

        # First byte is always 0, 512 after that is the 512 channels
        self.dmx_message = array('B', [0] * 513)

    def set_channels(self, message):
        """
        a dict and writes them to the array
        format {channel:value}
        """

        for ch in message:
            self.dmx_message[ch] = message[ch]

        # for i, ch in enumerate(channels):
        #     self.dmx_message[ch] = values[i]

    def write_frame(self):
        """
        Send a DMX frame
        """
        # DMX needs a 88us low to begin a frame,
        # 77uS us used because of time it takes to init pin
        dmx_uart = Pin(21, Pin.OUT)
        dmx_uart.value(0)
        sleep_us(74)
        dmx_uart.value(1)

        # Now turn into a UART port and send DMX data
        #dmx_uart = UART(self.port)
        #dmx_uart.init(250000, bits=8, parity=None, stop=2)
        dmx_uart = UART(1)
        dmx_uart.init(250000, bits=8, parity=None, stop=2, rx=20, tx=21)
        #send bytes
        dmx_uart.write(self.dmx_message)
        #Delete as its going to change anyway
        del(dmx_uart)