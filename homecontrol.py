#HomeControl#

#####IMPORTS#####

#####def#########
def filereset():
    setupdat=setupr.read lines()
#####SETUP#######
print("HOMECONTROL")
setupr = open("setup.dat")
setupw = open("setup.dat", "w")
setupr.open()