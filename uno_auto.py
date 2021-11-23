#from arduino import pwr_to_pin
from datetime import datetime
from gtts import gTTS
from os import system
from time import sleep
from homecontrollib import *
mute=[False,False]
def run():
    if (datetime.now().strftime('%H:%M:%S')=='12:30:00' or datetime.now().strftime('%H:%M:%S')=='12:30:01' or datetime.now().strftime('%H:%M:%S')=='12:30:02' or datetime.now().strftime('%H:%M:%S')=='12:30:03'):
        #pwr_to_pin(8,1,0)
        myobj = gTTS(text="It is "+datetime.now().strftime('%H:%M'), lang='en', slow=False)
        myobj.save('gtts.mp3')
        system('start gtts.mp3')
        sleep(60)
        new_msg('ON','uno auto')
    if (datetime.now().strftime('%H:%M')=='12:35'):
        #pwr_to_pin(8,0)
        myobj = gTTS(text="It is "+datetime.now().strftime('%H:%M'), lang='en', slow=False)
        myobj.save('gtts.mp3')
        system('start gtts.mp3')
        new_msg('OFF','uno auto')
        sleep(60)
