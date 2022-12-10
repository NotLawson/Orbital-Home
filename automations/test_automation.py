from homecontrollib import *
#from automations import auto_util
name="test_automation"

async def start():
    await time(12,55)
    new_msg("Time is 12:55",name,"INFO")
    start_automation(name)
    
    