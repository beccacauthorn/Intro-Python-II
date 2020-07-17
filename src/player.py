# Write a class to hold player information, e.g. what room they are in
# currently.
#Add capability to add `Item`s to the player's inventory. The inventory can
#also be a `list` of items "in" the player, similar to how `Item`s can be in a
#`Room`.
class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items
