#!/usr/bin/env python3

## lib to generate UUID's
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

for rando in range(howmany):
    print( uuid.uuid4() )
