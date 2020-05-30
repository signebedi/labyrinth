#!/usr/bin/env python

import json, time

header = [
    '  _           _                _       _   _     ',
    ' | |         | |              (_)     | | | |    ',
    ' | |     __ _| |__  _   _ _ __ _ _ __ | |_| |__  ',
    " | |    / _` | '_ \| | | | '__| | '_ \| __| '_ \ ",
    ' | |___| (_| | |_) | |_| | |  | | | | | |_| | | |',
    ' |______\__,_|_.__/ \__, |_|  |_|_| |_|\__|_| |_|',
    '                     __/ |                       ',
    '                    |___/                        '
]

for item in header: print(item)

print("Welcome to LABYRINTH ! The evil king MINOS has invaded the ancient city of ATHENS and enforces his rule through his son, the cruel MINOTAUR ! It is up to YOU to save the city and defeat the evil monster ! But beware... you must traverse the depths of the LABYRINTH to find and defeat your foe. Good luck !")

class Player():
    def __init__(self): # here we start by building all of the player statistics that we would like to use throughout the game
        self.hp = 10
        self.lvl = 1
        self.xp = 0
        self.kills = 0
        self.str = 1
        self.int = 1
        self.con = 1
        self.gold = 5
        self.location = "Town"
        self.is_alive = True
        self.name = input('\nWhat is your name?\n> ')
    def name(self):
        self
    def stats(self):
        self.stat = f'\nname: {self.name}\nlocation: {player.location}\n\nhp: {self.hp} \nxp: {self.xp}\nlvl: {self.lvl}\nkills: {self.kills}\n\nstr: {self.str}\nint: {self.int}\ncon: {self.con}\ngold: {self.gold}'

### IN THE FUTURE, WE SHOULD ADD ASCII ART THAT SHOWS THE CHARACTER AND THE ARMOUR THEY'RE WEARING

        return self.stat


    def work(self, _time):
        self.work_time = round(time.time())+_time
        num = round(time.time())
        while(round(time.time()) <= self.work_time):
            # print (round(self.time - time.time()), end='\r')
            if round(time.time()) == num: pass
            else: print(round(self.work_time) - round(time.time()))
        self.gold += _time
        
    def counter(self):   
        num = round(time.time())                            
        while True:
            if num == round(time.time()): pass
            else:
                num = round(time.time())                                                                                                                                                                      
                print(num)
                
    def store(self):
        self.mode = 'store'
        print('\nyou walk into the general store to buy some goods\n')
        while self.mode == 'store':
            i = input('What would you like to buy? ')
            if i == "options": pass
            elif i == "upgrade str": pass
            elif i == "upgrade con": pass
            elif i == "upgrade int": pass
            elif i == "upgrade sword": pass
            elif i == "upgrade shield": pass
            elif i == "upgrade armor":pass
            elif i == "leave": print('\nyou left the general store\n'); self.mode = 'walking'
            else: print('\nUnknown command! Please try again\n')
    
    def battle(self):
        pass

    def dead(self):
        print(f'\nOh dear, {self.name}... it looks like you have been defeated. Better luck next time.\n')
        self.end_text = [
            ' ________         ____        __  __',
            '/_  __/ /  ___   / __/__  ___/ / / /',
            ' / / / _ \/ -_) / _// _ \/ _  / /_/ ',
            '/_/ /_//_/\__/ /___/_//_/\_,_/ (_)  \n\n',
        ]
        for item in self.end_text:print(item)
        self.is_alive = False


class WalkingMode():
    def __init__(self):
        self.move=''
        self.test=True

player = Player()

print(f"\nWelcome to Labyrinth, {player.name}!\n") 


def main():
    if player.hp <= 0: player.dead()
    while player.is_alive:
        i = input('\nWhat would you like to do next?\n> ')
        print(i)
        if i == 'quit': player.dead()
        elif i == 'stats': print(player.stats())
        elif i == 'work': time = input('work for how long?\n> '); player.work(int(time))
        elif i == 'count': player.counter()
        elif i == 'store': player.store()
        else: print('\nUnknown command! Please try again\n')

if __name__ == '__main__':
    main()