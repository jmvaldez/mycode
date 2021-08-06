#!/usr/bin/env python3

def getFile():
    with open("numfile.txt", "r") as numfile:
        numlist = []
        for line in numfile:
            numlist.append(int(line))
        return numlist

def main():
    for num in getFile():
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

if __name__ == "__main__":
    main()
