#HomeControl#

#####IMPORTS#####
import importlib as imp
from datetime import datetime
from homecontrollib import *
#####def#########
name='HOME_CONTROL'
message_state = ["","","",]
mute=[False, False]
message_structure=(message_state[0]+" -- "+message_state[1]+": "+message_state[2])

####SETUP#######
print("HOME CONTROL")
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
    imp.import_module(addons[addon_add])
    addon_add+=1
    
    
new_msg("Checking for Automations...",name)
exec(setup_content[3])
automation_num = int(setup_content[4])
automation_add = 0
while (automation_add<automation_num):
    imp.import_module(automations[0])
    automation_add+=1

new_msg("STARTING...",name)
home_run = 0
home_run_2_auto = int(setup_content[4])
home_run_3_app = int(setup_content[2])
import uno_auto
new_msg('STARTED',name)
while (0==0):
    run=(automations[home_run]+'.run()')
    exec(run)
    home_run+=1
    if (home_run==home_run_2_auto):
        home_run=0