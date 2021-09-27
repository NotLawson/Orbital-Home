####TEST####
name="TEST"
message_state = ["","","",False]
"Hi, im lawson"
from datetime import datetime
message_state = ["","","",]
mute=[False, False]
message_structure=(message_state[0]+" -- "+message_state[1]+": "+message_state[2])
def new_msg(message):
    global name
    message_state[0] = str(datetime.now().strftime('%H:%M:%S'))
    message_state[1] = name
    message_state[2] = message
    if (mute[1]==False):
        print(message_state[0]," -- ",message_state[1],": ",message_state[2])
    if (mute[0]==False):
        mdlgw=open('mod.txt', 'w')
        mdlgw.write(message_structure)
new_msg("hi my name is lawson")