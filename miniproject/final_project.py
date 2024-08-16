#!/usr/bin/python3

import random

def showInstructions():
    """
    Display the game instructions and available commands.
    """
    print('''
RPG Game
========
Commands:
  go [pick a direction either north, south, east, or west ]
  get [item having items may come in handy for your survial or maybe not  MUHAHAHAH! ]
  teleport [remember rooms that you have encoutnered for a way to fast travel ]
  look [to possibly uncover clues in your surroundings]
''')

def showStatus():
    """
    Display the player's current status including room description, inventory, and visible items.
    """
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(player.inventory))
    if 'description' in rooms[currentRoom]:
        print(rooms[currentRoom]['description'])
    if 'items' in rooms[currentRoom] and rooms[currentRoom]['items']:
        print('You see: ' + ', '.join(rooms[currentRoom]['items']))
    print("---------------------------")

def lookAtItem(item):
    """
    Display the description of a specific item if available.
    
    :param item: Name of the item to describe.
    """
    if item in itemsDescriptions:
        print(itemsDescriptions[item])
    else:
        print('You can\'t look at that.')

def teleportToRoom(room):
    """
    Teleport the player to a specified room if it exists.
    
    :param room: The room to teleport to.
    """
    global currentRoom
    if room in rooms:
        currentRoom = room
        print(f'Teleported to {room}')
    else:
        print('Invalid room.')

def levelUp():
    """
    Increase the player's level and allow them to allocate points to attributes.
    """
    global player
    print(f'Congratulations! You have leveled up to Level {player.level}!')
    print('Allocate points to Strength, Intelligence, or Speed.')
    choice = input('Enter attribute (Strength, Intelligence, Speed): ').strip().lower()
    points = player.level  # Points available to allocate
    if choice in ['strength', 'intelligence', 'speed']:
        setattr(player, choice, getattr(player, choice) + points)
        print(f'You allocated {points} points to {choice.capitalize()}.')
    else:
        print('Invalid choice.')
    player.level += 1  # Increase level

# Player class to manage player state
class Player:
    def __init__(self):
        """
        Initialize the player with default attributes and an empty inventory.
        """
        self.inventory = []
        self.level = 1
        self.strength = 1
        self.intelligence = 1
        self.speed = 1

    def addItem(self, item):
        """
        Add an item to the player's inventory.
        
        :param item: The item to add.
        """
        self.inventory.append(item)

    def removeItem(self, item):
        """
        Remove an item from the player's inventory.
        
        :param item: The item to remove.
        """
        self.inventory.remove(item)

# Initialize player object
player = Player()

# Descriptions for items in the game
itemsDescriptions = {
    'key': 'A rusty old key.',
    'potion': 'A mysterious potion that glows faintly.',
    'monster': 'A fearsome beast with sharp claws.'
}

# Define rooms and their attributes
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key',
        'description': 'A grand hall with portraits on the walls.',
        'items': ['key']  # List of items in this room
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
        'description': 'A kitchen with a large stove and various utensils.',
        'items': ['monster']  # List of items in this room
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'description': 'A dining room with a long table and chairs.',
        'items': ['potion']  # List of items in this room
    },
    'Garden': {
        'north': 'Dining Room',
        'description': 'A beautiful garden with flowers and a fountain.',
        'items': []  # Empty list of items
    },
    'Library': {
        'east': 'Hall',
        'description': 'A quiet library filled with books.',
        'items': []  # Empty list of items
    },
    'Lab': {
        'west': 'Garden',
        'description': 'A laboratory with various scientific instruments.',
        'items': []  # Empty list of items
    }
}

# Start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# Counter for moves
moves = 0

# Main game loop
while True:
    showStatus()

    # Get the player's next command
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    if len(move) < 2:
        print('Invalid command. Try again.')
        continue

    if move[0] == 'go':
        # Handle movement between rooms
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            moves += 1  # Increment move counter
        else:
            print('You can\'t go that way!')

    elif move[0] == 'get':
        # Handle item pickup
        item = move[1]
        if 'items' in rooms[currentRoom] and item in rooms[currentRoom]['items']:
            player.addItem(item)
            rooms[currentRoom]['items'].remove(item)
            print(f'{item} got!')
            lookAtItem(item)
        else:
            print(f'Can\'t get {item}!')

    elif move[0] == 'teleport':
        # Handle teleport command
        teleportToRoom(move[1])
        moves += 1  # Increment move counter

    elif move[0] == 'look':
        # Handle looking at items or room description
        if len(move) > 1:
            lookAtItem(move[1])
        else:
            showStatus()

    else:
        print('Unknown command. Try again.')

    # Define win condition
    if currentRoom == 'Garden' and 'key' in player.inventory and 'potion' in player.inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        print(f'Total moves: {moves}')
        break

    # Define loss condition for encountering a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        print(f'Total moves: {moves}')
        break

    # Level up every 10 moves
    if moves % 10 == 0:
        levelUp()
