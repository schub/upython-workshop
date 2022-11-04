import ssd1306
from machine import Pin, SoftI2C

oled_width = 128
oled_height = 64

class Display:
    def __init__(self, pin_scl, pin_sda):
        i2c = SoftI2C(scl=Pin(pin_scl), sda=Pin(pin_sda))
        self.oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
        self.title = '...'
        self.items = ['', '', '', '']
    
    def set_item(self, text, pos):
        if (pos >=0 and pos <4):
            self.items[pos] = text
    
    def set_title(self, title): 
        self.title = title

    def show(self):
        self.oled.fill(1)
        for x in range(oled_width):
            self.oled.pixel(x, 16, 0)
        self.oled.text(self.title, 0, 5, 0)
        for i in range(len(self.items)):
            self.oled.text(self.items[i], 0, i*10 + 22, 0)
        self.oled.show()


    def clear_items(self):
        self.items = ['', '', '', '']