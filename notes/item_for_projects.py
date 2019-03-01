class Player(object):
    def __init__(self, energy=100):
        self.energy = energy
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


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self) .__init__(name)
