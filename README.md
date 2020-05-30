# labyrinth
Labyrinth is a turn-based, textual role playing game written in python by Agni and Signe Bedi. 

*Welcome to LABYRINTH! The evil king MINOS has invaded the ancient city of ATHENS and enforces his rule through his son, the cruel MINOTAUR! It is up to YOU to save the city and defeat the evil monster! But beware... you must traverse the depths of the LABYRINTH to find and defeat your foe. Good luck, Young adventurer! You will need it!*

The game's primary executable is labyrinth.py, which will contain all of the necessary code to
run the game as a command-line executable. While version 1.0 of this program runs on vanilla
python, a requirements.txt file has been included in the repository for future versions.

In addition, we will include a save file -- as a JSON -- to preserve character
data between instances of the game.

Labyrinth is a CLI, object-oriented, and built around the Player class with multiple modes. Not to be 
confused with difficulty-levels, a mode provides decisions to the player based on the context 
of the game. For example, if a player is simply traversing the map, then the mode is Player.walk(),
and the options available to them will reflect that mode -- in this case they can move to a new
tile, find a monster to battle, etc. A list of some of the modes are below:

1. **Walking**: the player walks between locations
2. **Battle**: the player battles monsters train and earn money
3. **Store**: the player buys new weaponws and upgrades stats
4. **Work**: the player works for a time to earn money
5. **Save**: the player saves their stats for the next round
6. **Stats**: shows the player's statistics

The Map will be a procedural map built around a center point -- the town. This section is still
undergoing some development.


## To Do:
* fix work() mode so that it counts down appropriately
* finish store() mode
* merge walking() mode into the main game
* add battle() mode
* develop a system for random items to drop from monsters
* modify stats mode to show ASCII art of the character and their armor, as well as their kill count


Developer notes-to-self:
1. https://medium.com/@angellom/writing-a-python-dungeon-game-part-i-47e35668f16b 
2. https://github.com/gilles-leblanc/gameproject
3. https://inventwithpython.com/makinggames.pdf
4. https://github.com/grantjenks/free-python-games
5. https://github.com/topics/cli-game # Examples of CLI games on Github
6. https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/ # Excellent multi part tutorial for creating a CLI
7. https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df # creating a beautiful CLI using the Click library
8. https://github.com/asweigart/textadventuredemo # another *solid* example game from Al Sweigert 

-- Angus and Sig

