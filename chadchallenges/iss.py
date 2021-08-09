#!/usr/bin/env python3

import time

import requests

url = 'http://api.open-notify.org/iss-now.json'

def main():
   resp = requests.get(url).json()
   
   lat = resp["iss_position"]["latitude"]
   lng = resp["iss_position"]["longitude"]
   ts = resp["timestamp"]

   ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts))
    
   print(f"""
   ISS Location:
   Lat: {lat}
   Lng: {lng}
   time: {ts}""")

main() 

    
