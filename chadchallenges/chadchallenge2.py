#!/usr/bin/env python3
import random

icecream= ["flavors", "salty"]

tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

icecream.append(int(99))

rand_person = int(random.random() * len(tlgclass) )

select_user = input(f'Select a user between 0 and {len(tlgclass) - 1 }: ')

print(icecream[2], icecream[0], "and", tlgclass[rand_person], "chooses to be", icecream[1]  )
