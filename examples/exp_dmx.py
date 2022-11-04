import dmx
from time import sleep

dmx1 = dmx.universe(1)

for i in range(255):

    dmx1.set_channels({1:i,2:0,3:0})
    dmx1.write_frame()

    sleep(0.01)
    

for i in range(255):

    dmx1.set_channels({1:255,2:i,3:i})
    dmx1.write_frame()

    sleep(0.01)

for i in range(255):

    dmx1.set_channels({1:254-i,2:254-i,3:254-i})
    dmx1.write_frame()

    sleep(0.01)
    