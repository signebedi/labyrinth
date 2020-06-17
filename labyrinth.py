#!/usr/bin/env python
from items import items # this file contains a dictionary of all the available items in the game
from enemies import enemies # this file contains a dictionary of all the enemies you can fight in the game
from player import Player # this file contains the Player() class, which is the building block of the game
from dungeon import map # this file contains all map elements

import time, colorama
from colorama import Fore, Back, Style


def main():
    
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
    
    player = Player()

    print(f"\nWelcome to Labyrinth, {player.name}!\n") 

    
    while player.is_alive:
        i = input('\nWhat would you like to do next?\n> ')
        print(i)
        if i == 'quit': player.dead()
        elif i == 'stats': print(player.stats())
        elif i == 'hurt': player.hp -= 3; print('\noh no, you hurt yourself!\n')
        elif i == 'work': time = input('work for how long?\n> '); player.work(int(time))
        elif i == 'count': player.counter()
        elif i == 'store': player.store()
        elif i == 'move': player.move(map)
        elif i == 'fight': player.battle()
        else: print('\nUnknown command! Please try again\n')
    
        if player.hp <= 0: player.dead()


if __name__ == '__main__':
    main()