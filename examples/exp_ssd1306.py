from ssd1306 import SSD1306_I2C
from machine import Pin, SoftI2C
import time

# init oled display
i2c = SoftI2C(scl=Pin(10), sda=Pin(8))
oled = SSD1306_I2C(128,32,i2c)

# show some stuff
oled.fill(1)
oled.text('Hello World!', 5, 5, 0)
oled.show()

x = 1
y = 1
x_dir = 1
y_dir = 1

while True:
    oled.fill(1)
    oled.text('Hello World!', x, y, 0)
    oled.show()
    x += 3 * x_dir
    y += 2 * y_dir
    if (x >= 32 or x <= 1):
        x_dir = -1 * x_dir
    if (y >= 25 or y <= 1):
        y_dir = -1 * y_dir
    time.sleep(0.1)
