# labyrinth
Labyrinth is a turn-based, textual role playing game written in python by Agni and Signe Bedi. 


The game's primary executable is labyrinth.py, which will contain all of the necessary code to
run the game as a command-line executable. While version 1.0 of this program runs on vanilla
python, a requirements.txt file has been included in the repository for future versions.

In addition, we will include a save file -- either as a JSON or CSV -- to preserve character
data between instances of the game.

Labyrinth is a CLI, object-oriented, and built around different classes of GameModes. Not to be 
confused with difficulty-levels, a GameMode provides decisions to the player based on the context 
of the game. For example, if a player is simply traversing the map, then the GameMode is WalkingMode(),
and the options available to them will reflect that mode -- in this casem they can move to a new
tile, find a monster to battle, etc. A list of some of the GameModes are below:

    1. WalkingMode
    2. BattleMode
    3. StoreMode
    4. WorkMode
    5. SaveMode
    6. StatMode

The Map will be a procedural map built around a center point -- the town. This section is still
under development.

Developer notes-to-self:
    1. https://medium.com/@angellom/writing-a-python-dungeon-game-part-i-47e35668f16b 
    2. https://github.com/gilles-leblanc/gameproject
    3. https://inventwithpython.com/makinggames.pdf
    4. https://github.com/grantjenks/free-python-games
    5. https://github.com/topics/cli-game # Examples of CLI games on Github
    6. https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/ # Excellent multi part tutorial for creating a CLI
