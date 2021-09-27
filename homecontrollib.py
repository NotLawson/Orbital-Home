message_state = ["","","",]
message_structure=(message_state[0]+" -- "+message_state[1]+": "+message_state[2])
from datetime import datetime
def new_msg(message, name):   
    global mute
    message_state[0] = str(datetime.now().strftime('%H:%M:%S'))
    message_state[1] = name
    message_state[2] = message
    print(message_state[0]," -- ",message_state[1],": ",message_state[2])
    mdlgw=open('mod.txt', 'w')
    mdlgw.write(message_structure)

    