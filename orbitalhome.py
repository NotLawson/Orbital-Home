#HomeControl#

#####IMPORTS#####
import importlib as imp
from datetime import datetime
from homecontrollib import *
#####def#########
name='ORBITAL_HOME'
message_state = ["","","",]
mute=[False, False]
message_structure=(message_state[0]+" -- "+message_state[1]+": "+message_state[2])

####SETUP#######
print("ORBITAL HOME")
new_msg("Checking for pre-use...",name)
setup = open("setup.txt")
setup_content = setup.readlines()
setup.close()
exec(setup_content[0])
exec(setup_content[1])
if (ftu==True):   ###### Tutorial
    print("(needs work on)")
new_msg("Checking for add-ons...",name)
addonnum = int(setup_content[2])
addon_add = 0
while (addon_add<addonnum):
    ex='import '+addons[addon_add]
    #imp.import_module(addons[addon_add])
    exec(ex)
    addon_add+=1

new_msg("Adding Devices",name)
devices3=open('devices.txt')
devices2=devices3.readlines()
devices=int(devices2[0].strip('\n'))
exec(devices2[1].strip('\''))
for d in range(devices):
    device_info_2=open(device_names[d]+'.device')
    device_info_3=device_info_2.readlines()
    exec(device_info_3[0])
    if (device_info[1]=='arduino'):
        arduino.setup_device(d)
    device_type.append(device_info[2])


new_msg("Checking for Automations...",name)
exec(setup_content[3])
automation_num = int(setup_content[4])
automation_add = 0
while (automation_add<automation_num):
    ex = "import "+automations[automation_add]
    exec(ex)
    #imp.import_module(automations[automation_add])
    automation_add+=1

new_msg("STARTING...",name)
home_run = 0
home_run_2_auto = int(setup_content[4])
home_run_3_app = int(setup_content[2])
new_msg('STARTED',name)

while (0==0):
    run=(automations[home_run]+'.run()')
    exec(run)
    home_run+=1
    if (home_run==home_run_2_auto):
        home_run=0