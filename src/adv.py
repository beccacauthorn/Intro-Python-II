from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("rope", "for climbing"),
                      Item("lantern", "help guide the way"),
                      Item("sushi", "keep energy high")]
                      ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                [Item("dog", "this animal has special powers"),
                 Item("map", "mark your way"),
                 Item("backpack", "carries your supplies")]
                 ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                [Item("binoculars", "see far away"),
                 Item("pen", "take note of what you see"),
                 Item("boots", "keeps your feet cozy")]
                 ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                [Item("shovel", "digging help"),
                 Item("pick axe", "more digging help"),
                 Item("metal detector", "find the treasure quicker")]
                 ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [Item("metal chest", "where the treasure is hidden"),
         Item("letters", "found at bottom of chest"),
         Item("locket with picture", "only clue as to whom the treasure belonged to")]
         ),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Wizard", room['outside'], [])

# Write a loop that:
while True:
    # * Prints the current room name
    print(player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.desc)
    #print current_room items
    print("These are the items available to you in this room: ")
    for i in player.current_room.items:
        print(i)

    # * Waits for user input and decides what to do.
    command = input("What do you want to do? ")
    split_command = command.split(" ")

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if len(split_command) == 1:
        if command == "n":
            # move north if possible
            if player.current_room.n_to is None:
                print("There is nothing to the North.")
            else:
                player.current_room = player.current_room.n_to
        elif command == "s":
            if player.current_room.s_to is None:
                print("There is nothing to the South.")
            else:
                player.current_room = player.current_room.s_to
        elif command == "e":
            if player.current_room.e_to is None:
                print("There is nothing to the East.")
            else:
                player.current_room = player.current_room.e_to
        elif command == "w":
            if player.current_room.w_to is None:
                print("There is nothing to the West.")
            else:
                player.current_room = player.current_room.n_to
        # If the user enters "q", quit the game.
        elif command == "q":
            break
        else:
            print("Invalid command")
    elif len(split_command) == 2:
        if split_command[0] == "get" or split_command[0] == "take":
            # do something with player.current_room.items and split_commnad[1]
            len_before = len(player.current_room.items)
            for i, item in enumerate(player.current_room.items):
                if split_command[1] == item.name:
                    player.current_room.items.remove(item)
                    player.items.append(item)
                    item.on_take()
            if len_before == len(player.current_room.items):
                print("Could not find an item with that name")

        else:
            print("Invalid command")
        
