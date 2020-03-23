#!/usr/bin/env python

player = {}
player['hp'] = 10
player['lvl'] = 1
player['str'] = 1
player['int'] = 1
player['con'] = 1
player['is_alive'] = True

player['name'] = input('\nWhat is your name?\n> ')

print(f"\nWelcome to Labyrinth, {player['name']}!\n\nThe evil king MINOS as invaded the ancient city of ATHENS...\n") # Agni will write the rest of the back story for this section

# if player['input'] == 'help':
#   print(player['options']) #each GameMode will set different player options


class WalkingMode():
    def __init__(self):
        self.move=''

# class BattleMode():

# class StoreMode():

# class WorkMode():

# def MapGenerator(x=100,y=100): # this is where we will generate the map for each game
#    pass

def main():
    while player['is_alive']:
        player['input'] = input('\nWhat would you like to do next?\n> ')
        print(player['input'])

if __name__ == '__main__':
    main()
