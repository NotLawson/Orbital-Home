#HomeControl#

#####IMPORTS#####
from homecontrollib import *
import json
import asyncio
#####def#########
name='HOME_CONTROL'
version="indev"
####SETUP#######
print("HOME CONTROL ("+version+")")
json_setup = open("setup.json")
setup=json.load(json_setup)
json_setup.close()
new_msg("Loading addons...",name, "INFO")
addons = setup["addons"]
i = 0
for i in range(len(addons)):
    new_msg("Importing "+addons[i], name, "INFO")
    try:
        exec("from addons import "+addons[i])
        new_msg(addons[i]+" imported.", name, "INFO")
    except:
        new_msg(addons[i]+" import failed.", name, "ERROR")
    i=+1

    
new_msg("Loading automations...",name, "INFO")
auto = setup["automations"]
i = 0
for i in range(len(auto)):
    new_msg("Importing "+auto[i], name, "INFO")
    try:
        exec("from automations import "+auto[i])
        new_msg(auto[i]+" imported.", name, "INFO")
    except:
        new_msg(auto[i]+" import failed.", name, "ERROR")
    i=+1

new_msg('Starting Home control', name, 'INFO')
i=0
for i in range(len(addons)):
    new_msg("Staring "+addons[i], name, "INFO")
    try:
        exec(addons[i]+".start()")
        new_msg(addons[i]+" started.", name, "INFO")
    except:
        new_msg("failed to start "+addons[i], name, "ERROR")
    i=+1

i=0
for i in range(len(auto)):
    new_msg("Staring "+auto[i], name, "INFO")
    try:
        exec("asyncio.run("+auto[i]+".start())")
        new_msg(auto[i]+" started.", name, "INFO")
    except:
        new_msg("failed to start "+auto[i], name, "ERROR")
    i=+1
new_msg("test",name,"INFO")