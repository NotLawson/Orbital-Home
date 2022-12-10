from homecontrollib import *
#from addons import addon_util
name="Test"

def service(service):
    global name
    new_msg("Test service: name="+service,name,"INFO")
def start():
    new_msg('Test addon started',name,"INFO")