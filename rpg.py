#!/usr/bin/python3

from random import randint
import sys

class Player(object):
    def __init__(self):
        self.hp = 100
        self.inventory = {'axe': 1, 'bow': 1, 'bladeOfDoom': 0}
        self.action = {
                'slice': (randint(1,15), 'slice'),
                'shoot': (randint(3,12), 'shoot'),
                'smite': ( 50, 'smite')
                }

class Bandit():
    def __init__(self):
        self.hp = 30
        self.inventory = {'blade': 1}
        self.action = {
                'stab': (randint(2,15), 'stab')
                }


def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  stat [status]
  inv [inventory]
''')

def showStatus():
  player = Player()
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(player.inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

def playerAttack():
    player = Player()
    attackList = list(player.action.keys())
    attackChoice = input(f"How will you attack? {attackList} ")
    if attackChoice in attackList:
        print(player.action.get(attackChoice)[0])
    else:
        attackChoice = input(f"How will you attack? {attackList} ")
        print(player.action.get(attackChoice)[0])

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north': 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'
showInstructions()

while True:
    move = ''
    while move == '':
        move = input('>')

    
    ##playerAttack()
    if move[0] == "stat":
        showStatus()

    if move[0] in ['q', 'quit']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass

