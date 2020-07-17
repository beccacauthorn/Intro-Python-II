#Create a file called `item.py` and add an `Item` class in there.
# The item should have `name` and `description` attributes.
# Hint: the name should be one word for ease in parsing later.

class Item:
    def __init__(self, name, item_description):
        self.name = name
        self.item_description = item_description

    def __str__(self):
        return f'{self.name}: {self.item_description}'

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")