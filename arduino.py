#ARDUINO ADDON FOR HOME CONTROL#
name='arduino'
mute=[False, False]
from pyfirmata import Arduino, util
from datetime import datetime
from homecontrollib import *
new_msg("ADDON BOOTING",name)
bootfailreason="null"
try:
    ###Insert board name and port
    uno = Arduino("COM3")
    board_name = [uno]
    bootfail = False
except:
    bootfail=True
    bootfailreason="CAN'T FIND PORT OR SERIAL BROKEN"
if (bootfail==False):
    new_msg("ADDON BOOTED",name)
elif (bootfail==True):
    new_msg("ADDON CRASHED REASON: "+bootfailreason,name)
def pwr_to_pin(pin, state, board=0):
    global board_name
    board_name[board].digital[pin].write(state)
    new_msg("Pin "+str(pin)+" set to state "+str(state), name)
def a_read(pin, board=0):
    it = util.Iterator(board)
    it.start()
    board_name[board].analog[pin].enable_reporting()
    return board_name[board].analog[pin].read()
    