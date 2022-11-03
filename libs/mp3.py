from time import sleep
from machine import UART

uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1, rx=20, tx=21)

# set initial volume to mid point 
volume_level=15 

initialized=False

"""
	protocol defintion file for the CATALEX seriel MP3 player
	The board uses the YX5300 MP3 audio chip. It supports 8KHz to 48KHz sampling frequencies for MP3 and WAV file format
	
	Not all commands are mapped. 
	
	Command format
	
	Each command is 8 bytes
	Pos	Descrption 	Bytes	Value
	1 	Start		1		0x7E
	2	Version		1		0xFF
	3	Lenght		1		0x06
	4	Command		1		see below
	5	Feedback	1		0x00 for off, 0x01 On
	6	Data		2		depends of command
	8	End			1		0xEF
	
	Code 	Commands
	0x01	Next track
	0x02	Previous track
	0x03	Play with index, index given in data field
	0x04	Volume up by 1
	0x05	Volume down by 1
	0x06	Set volume to value provided in data field (0-30)
	0x0A	Put chip to sleep mode
	0x0B	Wake chip from sleep mode
	0x0C	Reset chip
	0x0D	Resume playback
	0x0E	Pause playback
	0x16	Stop playback
			
"""

def command_base():
	command=bytearray()
	command.append(0x7e)
	command.append(0xFF)
	command.append(0x06)
	command.append(0x00)
	command.append(0x00)
	command.append(0x00)
	command.append(0x00)
	command.append(0xEF)
	return command

# do necessary initialization
# Currently only the volume is set
def initialize():
	global initialized
	global volume_level
	if not initialized:
		set_volume(volume_level)
		initialized=True
		sleep(0.5)

def next():
	initialize()
	command=command_base()
	command[3]=0x01		
	uart.write(bytearray(command))

def previous():
	initialize()
	command=command_base()
	command[3]=0x02	
	uart.write(bytearray(command))

def hibernate():
	command=command_base()
	command[3]=0x0A	
	uart.write(bytearray(command))

def wakeup():
	command=command_base()
	command[3]=0x0B	
	uart.write(bytearray(command))
	
def reset():
	global initialized
	initialized=False
	command=command_base()
	command[3]=0x0C	
	uart.write(bytearray(command))
	
	
def play_track(track_id):
	initialize()
	command=command_base()
	command[3]=0x03
	command[6]=track_id
	uart.write(bytearray(command))

def play():
	initialize()
	play_track(1)
	
def pause():
	command=command_base()
	command[3]=0x0E
	uart.write(bytearray(command))

def resume():
	command=command_base()
	command[3]=0x0D
	uart.write(bytearray(command))
	
def stop():
	command=command_base()
	command[3]=0x16
	uart.write(bytearray(command))

def set_volume(level):
	global volume_level
	volume_level=level
	command=command_base()
	command[3]=0x06
	command[6]=level
	uart.write(bytearray(command))
	
def volume_up(step_count=1):
	global volume_level
	volume_level=volume_level+step_count
	set_volume(volume_level)
			
def volume_down(step_count=1):
	global volume_level
	volume_level=volume_level-step_count
	set_volume(volume_level)

def mute():
	command=command_base()
	command[3]=0x06
	command[6]=0
	uart.write(bytearray(command))
	
def unmute():
	global volume_level
	command=command_base()
	command[3]=0x06
	command[6]=volume_level
	uart.write(bytearray(command))
	

def get_volume():
	global volume_level
	return volume_level
