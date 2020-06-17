# this file contains a dictionary of all the available enemies in the game

enemies = [
    {"name": "Hunter", "hp": 10, "strength": "Earth", "weakness": "Fire",  "drops": ["Long Bow", "Arrow", "cooked morsel"]},
    {"name": "Scorpion", "hp": 7, "strength": "Water", "weakness": "Earth", "drops": ["Scorpion Tail", " coins"]},
    {"name": "Alien", "hp": 15, "strength": "Earth", "weakness": "Water", "drops": ["Alien Tail", "Potion", "coins"]},
    {"name": "Town Drunk", "hp": 5, "strength": "None", "weakness": "Fire", "drops": ["old shoe", "coins"]},
    {"name": "Robot", "hp": 15, "strength": "Storm Magic", "weakness": "water magic", "drops": ["metal", "coins"]},
    {"name": "Witch", "hp": 6, "strength": "none", "weakness": "fire magic", "drops": ["broom", "coins"]},
    {"name": "Lava Monster", "hp": 4, "strength": "fire magic", "weakness": "water magic", "drops": ["slime", "coins", "lava rock"]},
    {"name": "Ghoul", "hp": 4, "strength": "water magic", "weakness": "fire magic", "drops": ["bone", "coins"]},
    {"name": "Worm", "hp": 4, "strength": "water magic", "weakness": "fire magic", "drops": ["slime"]},
    {"name": "Shark", "hp": 4, "strength": "water magic", "weakness": "storm magic", "drops": ["shark tooth", "coins"]},
    {"name": "Ghost", "hp": 4, "strength": "none", "weakness": "water magic", "drops": ["ectoplasm", "coins"]},
    {"name": "Guppie", "hp": 3, "strength": "none", "weakness": "storm magic", "drops": ["raw fish"]},
    {"name": "Dog", "hp": 4, "strength": "none", "weakness": "fire magic", "drops": ["fur", "coins"]},
    {"name": "Gangsta", "hp": 7, "strength": "normal attack", "weakness": "storm magic", "drops": ["stolen items", "coins"]},
    {"name": "Electro", "hp": 7, "strength": "water magic", "weakness": "none", "drops": ["antenna", "coins"]},
    {"name": "Fire Mage", "hp": 5, "strength": "fire magic", "weakness": "water magic", "drops": ["fire mage stick", "coins"]},
    {"name": "Water Mage", "hp": 5, "strength": "water magic", "weakness": "fire magic", "drops": ["water mage stick", "coins"]},
    {"name": "Knight", "hp": 6, "strength": "none", "weakness": "none", "drops": ["sword", "coins"]},
    {"name": "Ultra Mage", "hp": 8, "strength": "none", "weakness": "none", "drops": ["ultimate mage stick", "coins"]},
    {"name": "Monkey", "hp": 5, "strength": "water magic", "weakness": "fire magic", "drops": ["monkey crown", "coins"]},
    {"name": "Storm Mage", "hp": 6, "strength": "storm magic", "weakness": "fire magic", "drops": ["mage stick", "coins"]},
    {"name": "Barbarian", "hp": 10, "strength": "swords", "weakness": "fire", "drops": ["potion", "iron sword", "wooden shield"]},
    {"name": "Whale", "hp": 6, "strength": "water magic", "weakness": "electric magic", "drops": ["blubber", "coins"]},
    {"name": "Zombie", "hp": 7, "strength": "fire", "weakness": "water magic", "drops": ["brain mush", "coins"]}
]


known_locations = {
    "Town":["Town Drunk", "Robot","Dog","Gangsta","Knight",],
    "Graveyard":["Witch", "Lava Monster", "Ghoul", "Ghost", "Fire Mage", "Water Mage", "Storm Mage", "Ultra Mage","Zombie",],
    "Forest":["Hunter", "Scorpion", "Alien", "Worm", "Barbarian","Monkey",],
    "Harbor":["Shark", "Guppie", "Whale",],
}