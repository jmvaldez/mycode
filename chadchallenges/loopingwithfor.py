#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

## func 1
for farm in farms:
    if farm.get("name") == "NE Farm":
        for animals in farm.get("agriculture"):
            print(animals)

## func 2
users_farm = input("Choose a farm: NE Farm. W Farm, SE Farm")

for farm in farms:
    if farm.get("name") == users_farm:
        for agriculture in farm.get("agriculture"):
            print(agriculture)



def filter_vegetables(vegetable):
    vegetables = ["carrots", "celery"]

    if(vegetable in vegetables):
        return False
    else:
        return True


## func 3
users_farm = input("Choose a farm: NE Farm. W Farm, SE Farm")

for farm in farms:
    if farm.get("name") == users_farm:
            no_veggies = filter(filter_vegetables, farm.get("agriculture"))
            for veg in no_veggies:
                print(veg)

