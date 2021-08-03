#!/usr/bin/env python3
"""Pushing files around using shutil and os from the standard library """

import shutil
import os

def main():
    ## Make the program start in the home user directory
    os.chdir('/home/student/mycode/')

    ## Copies the file from source to target destination 
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    ## Copies the entire tree directory from root down. source/dest
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()



