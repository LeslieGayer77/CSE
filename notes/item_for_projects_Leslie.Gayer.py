import random


class Player(object):
    def __init__(self, name, energy=100, health=100, resistance=100, weapon=None,
                 armor=None):
        self.name = name
        self.energy = energy
        self.health = health
        self.resistance = resistance
        self.weapon = weapon
        self.armor = armor
        self.dead = False
        self.awake = True
        self.inventory = []


class Character(object):
    def __init__(self, name, dialogue, health=75, resistance=75, weapon=None,
                 armor=None):
        self.name = name
        self.dialogue = dialogue
        self.health = health
        self.resistance = resistance
        self.weapon = weapon
        self.armor = armor
        self.dead = False
        self.awake = True
        self.bitten = False
        self.inventory = []

    def take_damage(self, damage: int):
        if self.armor.protection > damage:
            print("No damage is done because of great armor")
        else:
            self.health -= damage - self.armor.protection
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Enemy(Character):
    def __init__(self, name, dialogue, health, resistance, weapon, armor):
        super(Enemy, self).__init__(name, dialogue, health, resistance, weapon,
                                    armor)


class Zombie(Character):
    def __init__(self, name, dialogue, health, resistance, weapon, armor, bite):
        super(Zombie, self).__init__(name, dialogue, health, resistance, weapon, armor)
        self.resistance = resistance
        self.bite = bite


class Item(object):
    def __init__(self, name):
        self.name = name


class Car(Item):
    def __init__(self, name, gas_left, durability):
        super(Car, self) .__init__(name)
        self.gas_left = gas_left
        self.durability = durability


nc = Car("Neighbors car", 100, 100)
bdc = Car("Broken down car", 50, 50)


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


class Melee(Weapon):
    def __init__(self, name, damage, visibility, kill_count):
        super(Melee, self) .__init__(name, damage, visibility,)
        self.kill_count = kill_count


class Katana(Melee):
    def __init__(self):
        super(Katana, self) .__init__('Katana', 100, 100, 3)


class Machete(Melee):
    def __init__(self, kill_count):
        super(Machete, self) .__init__('Basic Machete', 100, 100, 2)
        self.kill_count = kill_count


class Bat(Weapon):
    def __init__(self, name, damage, visibility, knockout=False):
        super(Bat, self) .__init__(name,  damage, visibility,)
        self.knockout = knockout


class Woodbat(Bat):
    def __init__(self):
        super(Woodbat, self) .__init__('Woodbat', 50, 100)

    def hit_target(self, target):
        hit = random.randint(0, 100)
        if hit > 50:
            knockout = True
            target.take_damage(self.damage)
            target.self.awake = False
            print("You knocked them out and they received 50 damage")
        else:
            knockout = False
            target.take_damage(self.damage)
            print("They received 50 damage")


class Ironbat(Bat):
    def __init__(self):
        super(Ironbat, self) .__init__('Ironbat', 60, 100)

    def hit_target(self, target):
        hit = random.randint(0, 100)
        if hit > 80:
            knockout = True
            target.take_damage(self.damage)
            target.self.awake = False
            print("You knocked them out and they received 65 damage")
        else:
            knockout = False
            target.take_damage(self.damage)
            print("They received 65 damage")


class Armor(Item):
    def __init__(self, name, protectiong, protectionk, protectionb):
        super(Armor, self) .__init__(name)
        self.protectiong = protectiong
        self.protectionk = protectionk
        self.protectionb = protectionb


class BV(Armor):
    def __init__(self):
        super(BV, self) .__init__("Bulletproof Vest", 100, 0, 0)


class RG(Armor):
    def __init__(self):
        super(RG, self) .__init__("Riot Gear", 90, 50, 100)


class Key(Item):
    def __init__(self, name):
        super(Key, self) .__init__(name)


key = Key("Car Key")
key1 = Key("House Key")

sword = Weapon("Sword", 10, 100)
canoe = Weapon("Canoe", 42, 100)
wiebe_armor = Armor("Armor of the gods", 10000000000, 100000000, 10000000)

orc = Character("Orc", "hello human", 100, 75, sword, ("Generic Armor", 2))
orc2 = Character("Weibe", "I will smite you for your insulance", 10000, 10000, canoe,
                 wiebe_armor)

orc.attack(orc2)
orc2.attack(orc)
