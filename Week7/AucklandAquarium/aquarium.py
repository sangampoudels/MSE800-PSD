from singleton import SingletonMeta


class Aquarium(metaclass=SingletonMeta):

    def __init__(self):
        self.fish_inventory = {}

    def add_fish(self, fish):

        category = fish.get_category()

        if category in self.fish_inventory:
            self.fish_inventory[category] += 1
        else:
            self.fish_inventory[category] = 1

    def display_inventory(self):

        print("\nAquarium Fish Inventory:")

        for fish, count in self.fish_inventory.items():
            print(f"{fish} : {count}")