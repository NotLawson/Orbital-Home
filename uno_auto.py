from arduino import pwr_to_pin
from datetime import datetime
from gtts import gTTS
from os import system
from time import sleep
from homecontrollib import *
mute=[False,False]
def run():
    if (datetime.now().strftime('%H:%M')=='14:10'):
        pwr_to_pin(13,1,0)
        myobj = gTTS(text="It is "+datetime.now().strftime('%H:%M'), lang='en', slow=False)
        myobj.save('gtts.mp3')
        system('start gtts.mp3')
        sleep(60)
        new_msg('ON','uno auto')
    if (datetime.now().strftime('%H:%M')=='14:40'):
        pwr_to_pin(13,0)
        myobj = gTTS(text="It is "+datetime.now().strftime('%H:%M'), lang='en', slow=False)
        myobj.save('gtts.mp3')
        system('start gtts.mp3')
        new_msg('OFF','uno auto')
        sleep(60)
