message_state = ["","","",]
from datetime import datetime
def new_msg(message, name):   
    global board
    message_state[0] = str(datetime.now().strftime('%H:%M:%S'))
    message_state[1] = name
    message_state[2] = message
    message_structure=(message_state[0]+" -- "+message_state[1]+": "+message_state[2])
    print(message_state[0]," -- ",message_state[1],": ",message_state[2])
#     mdlgw=open('mod.txt', 'w')
    #mdlgw.write(message_structure)

new_msg('TEST', 'TESR')   