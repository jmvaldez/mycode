#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import yaml

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'Handshaking. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# Connects to and reboots each ip in the list passed
def devicereboot(iplist):

    for ip in iplist.keys():
        print(f"Connecting to...{ip}")
        print("REBOOTING NOW!")
    


# start our main script
def main():
    """called at runtime"""

    # reading in data from yaml file
    with open('devicecmd.yaml') as devicecmdfile:
        devicecmd = yaml.load(devicecmdfile)

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    devicereboot(devicecmd)

# call our main function
main()

