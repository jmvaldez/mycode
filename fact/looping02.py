#!/usr/bin/env python3

## open the file in read mode
dnsfile = open("dnsservers.txt", "r")

## create list of lines
dnslist = dnsfile.readlines()

## loop over lines
for svr in dnslist:
    ## print and end without a new line
    print(svr, end="")

## close the file
dnsfile.close()
