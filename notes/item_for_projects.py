class Player(object):
    def __init__(self, energy=100, resistance=100):
        self.energy = energy
        self.resistance = resistance
        self.dead = False
        self.inventory = []


class Zombie(object):
    def __init__(self, resistance=100, bite=100):
        self.resistance = resistance
        self.bite = bite


class Item(object):
    def __init__(self, name):
        self.name = name


class Car(Item):
    def __init__(self, name):
        super(Car, self) .__init__(name)
        self.engine_status = False
        self.fuel = 100


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


class Gun(Weapon):
    def __init__(self, name, damage, visibility, blocked):
        super(Gun, self) .__init__(name, damage, visibility)
        self.blocked = blocked


class Pistol(Gun):
    def __init__(self):
        super(Pistol, self) .__init__("Pistol", 90, 50, False)
        self.blocked = False


class Shotgun(Gun):
    def __init__(self):
        super(Shotgun, self) .__init__("Shotgun", 100, 100, False)
        self.blocked = False


class Knife(Weapon):
    def __init__(self, name, damage, visibility):
        super(Knife, self) .__init__(name, damage, visibility)


class KitchenKnife(Knife):
    def __init__(self):
        super(KitchenKnife, self) .__init__('Kitchen Knife', 50, 25)


class HuntingKnife(Knife):
    def __init__(self):
        super(HuntingKnife, self) .__init__('Hunting Knife', 50, 25)


class Machete(Weapon):
    def __init__(self):
        super(Machete, self) .__init__('Machete', 100, 100)


class Bat(Weapon):
    def __init__(self, name, damage=25, visibility=100, knockout=False):
        super(Bat, self) .__init__(name,  damage, visibility,)
        self.knockout = knockout


class Woodbat(Bat):
    def __init__(self):
        super(Woodbat, self) .__init__('Woodbat')


class Ironbat(Bat):
    def __init__(self):
        super(Ironbat, self) .__init__('Ironbat', 50, 100)


class Armor(Item):
    def __init__(self, name, protection):
        super(Armor, self) .__init__(name)
        self.protection = protection


class BV(Armor):
    def __init__(self):
        super(BV, self) .__init__("Bulletproof Vest", 100)
        self.blocked = True


class Key(Item):
    def __init__(self, name,):
        super(Key, self) .__init__(name)


key = Key("Car Key")
key1 = Key("House Key")
