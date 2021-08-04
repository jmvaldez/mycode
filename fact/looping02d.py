#!/usr/bin/env python3

with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        svr = svr.rstrip("\n") ## removing newline char

        ## svr ends with org
        if svr.endswith("org"):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")

        ## svr ends with com
        elif svr.endswith("com"):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
