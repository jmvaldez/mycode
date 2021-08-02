#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)

## display list1[1] prints second item
print(list1[1])

## new list
list2 = ["juniper"]

## combining both lists together
list1.extend(list2)

## display the first list that is now combined with the second list
print(list1)

## create list 3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

## append list1 by list3
list1.append(list3)

## display the new list
print(list1)

## display the list of IP addresses
print(list1[4])

## print first item of the list of IP's
print(list1[4][0])

## create a list of 5 animals
animals = ["fox", "fly", "Ant", "Bee", "Hen"]

print(animals)
