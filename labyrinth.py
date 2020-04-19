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
        self.str = 1
        self.int = 1
        self.con = 1
        self.gold = 5
        self.location = "Town"
        self.is_alive = True
        self.name = input('\nWhat is your name?\n> ')
    def name(self):
        self
    def input(self): pass
    def stats(self):
        self.stat = f'\nname: {self.name}\nlocation: {player.location}\n\nhp: {self.hp} \nlvl: {self.lvl}\nstr: {self.str}\nint: {self.int}\ncon: {self.con}\ngold: {self.gold}'
        return self.stat


    def work(self, _time):
        self.time = round(time.time())+_time
        while(round(time.time()) <= self.time):
            print (round(self.time - time.time()), end='\r')
        self.gold += _time


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

# class EnemyGeneratorMode():
    # this was an idea I had: why don't we make it an option for a player to permanently generate a new
    # enemy and to save it to a player_generated_enemies.json file

# class BattleMode():

# class StoreMode():

# class WorkMode():
# class EnemyGeneratorMode():
    # this was an idea I had: why don't we make it an option for a player to permanently generate a new
    # enemy and to save it to a player_generated_enemies.json file

# class BattleMode():

# class StoreMode():

# class WorkMode():


player = Player()

print(f"\nWelcome to Labyrinth, {player.name}!\n") 


def main():
    while player.is_alive:
        i = input('\nWhat would you like to do next?\n> ')
        print(i)
        if i == 'die':player.dead()
        elif i == 'stats':print(player.stats())
        elif i == 'work': time = input('work for how long?\n> '); player.work(int(time))

if __name__ == '__main__':
    main()