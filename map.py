# class MapGenerator(x=100,y=100): # this is where we will generate the map for each game
    # def __init__(self):
        # here we want to build a map similar to the one below that 
        # is callable using positional notation.
# map = [
# 'x xxxxxxxxx x',
# 'x      xxxx x',
# 'xxxx   x xx x',
# 'xxxxxx x    x',
# 'xxxx x x xxxx',
# 'xxxx x x xxxx',
# 'xxxx   x xxxx'
# ]
# print(map[0][2]) # this will return 'x', which we can incorporate into our movement logic
import random
from enemies import enemies

class Map:
    def __init__(self):
        self.static = {
            "Town": ["Graveyard", "Forest", "Harbor"],
            "Graveyard": ["Town"],
            "Forest": ["Town"],
            "Harbor": ["Town"],
        }
    def move(self, location):
        try: 
            print(self.static[location],'\n')
            self.attacked = random.randint(1,48)
            if self.attacked <= 24: print(f"\nyou've been attacked by a {enemies[self.attacked]['name']}")
        except:
            print('no such location available')

        move = input('what do you want to do next:\n> ')
        self.move(move)

temp = Map()
temp.move("Town")