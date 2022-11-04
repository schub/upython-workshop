import mp3
from time import sleep

mp3.set_volume(20)

mp3.play_track(3)
sleep(10)
mp3.next()