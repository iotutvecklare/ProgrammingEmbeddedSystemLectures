import dog
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def __str__(self):
        return self.name + ": " + self.description

class Destructible:
    def __init__(self, durability):
        self.durability = durability

    def get_durability(self):
        return self.durability

class Weapon(Item, Destructible):
    def __init__(self, name, description, damage):
        Item.__init__(self, name, description)
        Destructible.__init__(self, durability=100)
        # super().__init__(name, description)
        self.damage = damage

    def get_damage(self):
        return self.damage

    def __str__(self):
        return f"{self.name}: {self.description}: Damage: {self.damage}"


if __name__ == '__main__':
    power_suit = Item(name="Power Suit", description="A suit that makes you so powerful that space marines looks like ants")
    heavy_bolder = Weapon(name="Heavy_bolter", description="A weapon that looks intimidating, but the damage is even more extreme", damage=90)
    print(power_suit)
    print(heavy_bolder)
    dog1 = dog.Dog("Doris", 15, "Poodle")
    dog1.bark()
    print(dog1.age_in_dog())
