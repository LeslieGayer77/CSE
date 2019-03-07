import random


class Player(object):
    def __init__(self, energy=100, resistance=100):
        self.energy = energy
        self.resistance = resistance
        self.inventory = []


class Item(object):
    def __init__(self, name):
        self.name = name


class Car(Item):
    def __init__(self, name, milage):
        super(Car, self) .__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.milage = milage


class Food(Item):
    def __init__(self, name, energy=0):
        super(Food, self) .__init__(name)
        self.energy = energy


class Junk(Food):
    def __init__(self):
        super(Junk, self).__init__('Junk Food', 25)


class Cans(Food):
    def __init__(self):
        super(Cans, self).__init__('Canned Food', 50)


class Weapon(Item):
    def __init__(self, name, damage, visibility):
        super(Weapon, self) .__init__(name)
        self.damage = damage
        self.visibility = visibility


class Knife(Weapon):
    def __init__(self):
        super(Knife, self) .__init__('Knife', 50, 25)


class Machete(Weapon):
    def __init__(self):
        super(Machete, self) .__init__('Machete', 100, 100)


class Bat(Weapon):
    def __init__(self):
        super(Bat, self) .__init__('bat', 25, 100)
        hit = random.randint(1, 2)
        if hit == 1:
            hit = True
            print("They took 25 damage and where knocked out")
        if hit == 2:
            hit = False
            print("They took 25 damage")


class Woodbat(Bat):
    def __init__(self):
        super(Woodbat, self) .__init__('Woodbat', 25, 100)


class Ironbat(Bat):
    def __init__(self):
        super(Ironbat, self) .__init__('Ironbat', 50, 100)


class Key(Item):
    def __init__(self, name,):
        super(Key, self) .__init__(name)
