#!/usr/bin/env python3

## creating a list
my_list = [ "192.168.0.5", 5060, "UP" ]

##Printing the first item of the list
print("The first item in the list (IP): " + my_list[0] )

## Printing second item of the list
## Second item is an int so cast as string
print("The second item in the list (port): " + str(my_list[1]) )

## Return last item of the list
print("The second item in the list (state): " + str(my_list[2]) )

## Challenge
## display only the ip addresses on the screen
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print(f"IP addresses: {iplist[3]}, and {iplist[4]}")


        

