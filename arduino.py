#ARDUINO ADDON FOR HOME CONTROL#
name='arduino'
mute=[False, False]
from pyfirmata import Arduino, util, STRING_DATA
from datetime import datetime
from homecontrollib import *
new_msg("ADDON BOOTED",name)
device_names=[]
def device(device, cmd):
    global board_name
    board_name[board].digital[pin].write(state)
    new_msg("Pin "+str(pin)+" set to state "+str(state), name)
def a_read(pin, board=0):
    it = util.Iterator(board)
    it.start()
    board_name[board].analog[pin].enable_reporting()
    return board_name[board].analog[pin].read()
def lcd_write(text, board):
    board_name[board].send_sysex( STRING_DATA, util.str_to_two_byte_iter(text) )
def setup_device(num):
    global board_name
    global device_names
    global board_commands
    device_list=open('devices.txt')
    device_list_2=device_list.readlines()
    z=0
    
    
    exec("devices="device_list_2[0].strip('\n'))
    for z in range(devices):
        device_list_2[z]=device_list_2[z].strip('\n')
    device_info=device_list_2
    device_name=str(device_info[0])+"."+str(device_info[1])
    new_msg("LOADING...",device_name)
    device_names.append(device_name)
    ex = device_name+'=Arduino(device_info[5])'
    exec(ex)
    ex = 'board_name.append('+device_name+')'
    exec(ex)
    new_msg("DONE",device_name)

setup_device(1)