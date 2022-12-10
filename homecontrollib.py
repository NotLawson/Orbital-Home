message_state = ["","","",]
from datetime import datetime
import time as t
def new_msg(message, name, msg_error):   
    message_state[0] = str(datetime.now().strftime('%H:%M:%S'))
    message_state[1] = name
    message_state[2] = message
    message_structure=message_state[0]+" -- "+"("+msg_error+") "+message_state[1]+": "+message_state[2]
    print(message_state[0]," -- ","(",msg_error,") ",message_state[1],": ",message_state[2])
    mod=open("mod.txt","a")
    mod.write(message_structure+"\n")