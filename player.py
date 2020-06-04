import time, colorama
from colorama import Fore, Back, Style


class Player():
    def __init__(self): # here we start by building all of the player statistics that we would like to use throughout the game
        colorama.init(autoreset=True)
        self.lvl = 1
        self.xp = 0
        self.kills = 0
        self.str = 1
        self.int = 1
        self.con = 1
        self.hp = 10*(self.lvl+self.con)
        self.gold = 5
        self.location = "Town"
        self.mode = 'walking'
        self.is_alive = True
        self.inventory = ['loincloth', 'woodenshield', 'healthpotion', 'bastardsword']
        self.equipped = {'weapon':'bastardsword', 'armor':'loincloth','shield':'woodenshield'}
        self.name = input('\nWhat is your name?\n> ')
    def inv(self):
        equipped = str(", ".join([x for x in self.inventory if x in self.equipped.values()]))
        unequipped = str(", ".join([x for x in self.inventory if x not in self.equipped.values()]))
        equip_list = Fore.CYAN + Style.BRIGHT + equipped + Style.RESET_ALL + " " + unequipped
        return equip_list
        
    def stats(self):
        if self.hp <= .25*(10*(self.lvl+self.con)): hp_color =  Fore.RED
        elif self.hp >= .75*(10*(self.lvl+self.con)): hp_color = Fore.GREEN 
        else: hp_color = Fore.YELLOW
        
        self.stat = f'\nname: ' + Fore.CYAN + Style.BRIGHT + f'{self.name}' + Style.RESET_ALL + f'\nlocation: {self.location}\n\nhp: '+ hp_color + Style.BRIGHT + f'{self.hp}' + Style.RESET_ALL + f' \nxp: {self.xp}\nlvl: {self.lvl}\nkills: {self.kills}\n\nstr: {self.str}\nint: {self.int}\ncon: {self.con}\ngold: {self.gold}\n\nInventory: {self.inv()}'

### IN THE FUTURE, WE SHOULD ADD ASCII ART THAT SHOWS THE CHARACTER AND THE ARMOUR THEY'RE WEARING

        return self.stat


    def work(self, _time):
        self.work_time = round(time.time())+_time
        num = round(time.time())
        while(round(time.time()) <= self.work_time):
            # print (round(self.time - time.time()), end='\r')
            if round(time.time()) == num: pass
            else: print(round(self.work_time) - round(time.time())); time.sleep(1)
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