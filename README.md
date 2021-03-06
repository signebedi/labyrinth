# labyrinth
Labyrinth is a turn-based, textual role playing game written in python by Agni and Signe Bedi. 

## Description:
Welcome to LABYRINTH! The evil king MINOS has invaded the ancient city of ATHENS and enforces his rule through his son, the cruel MINOTAUR! It is up to YOU to save the city and defeat the evil monster! But beware... you must traverse the depths of the LABYRINTH to find and defeat your foe. Good luck, dear adventurer! You will need it!

## Overview:
The game's primary executable is labyrinth.py, which will contain all of the necessary code to 
run the game as a command-line executable. While version 1.0 of this program runs on vanilla
python, a requirements.txt file has been included in the repository for future versions.

Labyrinth is a CLI, object-oriented, and built around the Player class with multiple game modes. Not to be 
confused with difficulty-levels, a mode provides decisions to the player based on the context 
of the game. For example, if a player is simply traversing the map, then the mode is Player.walk(),
and the options available to them will reflect that mode -- in this case they can move to a new
tile, find a monster to battle, etc. A list of some of the modes are below:

1. **Walking**: the player walks between locations
2. **Battle**: the player battles monsters train and earn money
3. **Store**: the player buys new weaponws and upgrades stats
4. **Work**: the player works for a time to earn money
5. **Save**: the player saves their stats for the next round
6. **Stats**: shows the player's statistics and allows them to modify their inventory
7. **Inventory**: the player can review their inventory, equip and unequip items, see how different items affect their stats, and make upgrades to certain items

The Map will be a procedural map built around a center point -- the town. This section is still
undergoing some development.


## Debugging
To make calls to inventory items, use the following syntax:
<pre><code>items[0]['description']</pre></code>

To make calls to the list of enemies, use the following syntax:
<pre><code>enemies[0]['name']</pre></code>

To debug, import the code into the python interactive prompt:
<pre><code>from player import Player
from enemies import enemies
from items import items</pre></code>

Then you can create a Player object and list all its available properties:
<pre><code>player = Player()
dir(player)</pre></code>


## To Do:
* <strike>fix work() mode so that it counts down appropriately</strike> finished 6.2.2020
* <strike>add some initial items to items.py and integrate into labyrinth.py</strike> finished 6.2.2020
* <strike>merge walking() mode and the static map into the main game, currently in map.py </strike> finished 6.8.2020
* <strike>select ASCII images to use for weapon, armor, shield, helmet (use color coding to distinguish between unique items); merge ASCII images into player.py; delete ASCII.txt</strike>  finished 6.8.2020
* <strike>add battle() mode</strike> finished 6.16.2020
* develop logic for spellbook and inventory
* add player inventory interface to equip different items, and incorporate equipment ASCII art into the interface
* finish store() mode
* add save() mode
* develop a system for random potions and special items to drop from monsters

## Video game resources for Angus:
1. https://medium.com/@angellom/writing-a-python-dungeon-game-part-i-47e35668f16b 
2. https://github.com/gilles-leblanc/gameproject
3. https://inventwithpython.com/makinggames.pdf
4. https://github.com/grantjenks/free-python-games
5. https://github.com/topics/cli-game # Examples of CLI games on Github
6. https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/ # Excellent multi part tutorial for creating a CLI
7. https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df # creating a beautiful CLI using the Click library
8. https://github.com/asweigart/textadventuredemo # another *solid* example game from Al Sweigert 

-- Angus and Sig

