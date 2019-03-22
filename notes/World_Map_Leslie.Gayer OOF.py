import random


class Room(object):
    def __init__(self, name,  description, north=None,  east=None, south=None,
                 west=None, northeast=None, northwest=None,  southeast=None,
                 southwest=None):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        self.characters = []


class Player(object):
    def __init__(self, name, starting_location, energy=100, health=100,
                 resistance=100, weapon=None, armor=None):
        self.name = name
        self.current_location = starting_location
        self.energy = energy
        self.health = health
        self.resistance = resistance
        self.weapon = weapon
        self.armor = armor
        self.dead = False
        self.awake = True
        self.bitten = False
        self.inventory = []

    def move(self, new_location):
        """ This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """
        This method  searches the current room so see if a room
        exists in that direction

        :param direction: The direction you want to move to
        :return: The room object if it exists, or none if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        if name_of_room == "ncar" and "key" not in player.inventory:
            print("You don't have the keys")
            return None
        return globals()[name_of_room]


class Character(object):
    def __init__(self, name, dialogue, health=100, resistance=75, weapon=None,
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

# def take_damage1(self, damage):
#   self.health = self.health - (damage - (self.resistance - self.armor.protection))


class Enemy(object):
    def __init__(self, name, dialogue, health=75, resistance=75, weapon=None):
        self.name = name
        self.dialogue = dialogue
        self.health = health
        self.resistance = resistance
        self.weapon = weapon
        self.dead = False
        self.awake = True
        self.bitten = False
        self.inventory = []


class Zombie(object):
    def __init__(self, resistance=None, attack=None):
        self.resistance = resistance
        self.attack = attack
        self.bite = False


class Item(object):
    def __init__(self,  name):
        self.name = name


class Car(Item):
    def __init__(self, name,  gas_left,  durability):
        super(Car, self).__init__(name)
        self.gas_left = gas_left
        self.durability = durability


nc = Car("Neighbors car", 100, 100)
bdc = Car("Broken down car", 50, 50)


class Food(Item):
    def __init__(self,  name,  energy=0):
        super(Food, self).__init__(name)
        self.energy = energy


class Junk(Food):
    def __init__(self):
        super(Junk, self).__init__('Junk Food', 25)


class Cans(Food):
    def __init__(self):
        super(Cans, self).__init__('Canned Food', 50)


class Weapon(Item):
    def __init__(self, name, damage, visibility):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.visibility = visibility


class Gun(Weapon):
    def __init__(self,  name, damage, visibility, blocked):
        super(Gun, self).__init__(name, damage, visibility)
        self.blocked = blocked


class Pistol(Gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", 90, 50, False)
        self.blocked = False


class Shotgun(Gun):
    def __init__(self):
        super(Shotgun, self).__init__("Shotgun", 100, 100, False)
        self.blocked = False


class Knife(Weapon):
    def __init__(self, name, damage, visibility):
        super(Knife, self).__init__(name, damage, visibility)


class KitchenKnife(Knife):
    def __init__(self):
        super(KitchenKnife, self).__init__('Kitchen Knife', 50, 25)


class HuntingKnife(Knife):
    def __init__(self):
        super(HuntingKnife, self).__init__('Hunting Knife', 50, 25)


class Melee(Weapon):
    def __init__(self, name, damage, visibility, kill_count):
        super(Melee, self).__init__(name, damage, visibility, )
        self.kill_count = kill_count


class Katana(Melee):
    def __init__(self):
        super(Katana, self).__init__('Katana', 100, 100, 3)


class Machete(Melee):
    def __init__(self, kill_count):
        super(Machete, self).__init__('Basic Machete', 100, 100, 2)
        self.kill_count = kill_count


class Bat(Weapon):
    def __init__(self, name, damage, visibility, knockout=False):
        super(Bat, self).__init__(name, damage, visibility, )
        self.knockout = knockout


class Woodbat(Bat):
    def __init__(self):
        super(Woodbat, self).__init__('Woodbat', 50, 100)

    def hit_target(self, target):
        hit = random.randint(0, 100)
        if hit > 50:
            knockout = True
            target.take_damage
            target.self.awake = False
            print("You knocked them out and they received 50 damage")
            if hit < 50:
            knockout = False
            target.take_damage
            print("They received 50 damage")

    def hit_target(self, target):
        if self.armor == 'RG':
            print("No damage is done because of great armor")
        else:
            self.health -= damage - self.armor.protection
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Ironbat(Bat):
    def __init__(self):
        super(Ironbat, self).__init__('Ironbat', 50, 100)
        hit = random.randint(0, 100)
        if hit > 30:
            knockout = True
            print("You knocked them out and they received 50 damage")
        if hit < 30:
            knockout = False
            print("They received 60 damage")


class Armor(Item):
    def __init__(self, name, protectiong, protectionk, protectionb):
        super(Armor, self).__init__(name)
        self.protectiong = protectiong
        self.protectionk = protectionk
        self.protectionb = protectionb


class BV(Armor):
    def __init__(self):
        super(BV, self).__init__("Bulletproof Vest", 100, 0, 0)


class RG(Armor):
    def __init__(self):
        super(RG, self).__init__("Riot Gear", 90, 50, 100)


class Key(Item):
    def __init__(self, name):
        super(Key, self).__init__(name)

Dean = Character("Dean", "HOwdy", 100, 100, Machete(1), BV(), )
Sam = Character("Sam", "No hablo espanol", 100, 90, Pistol(), RG(), )
# Option 1 - define as we go
# R19A = Room("Mr. Weibe's Room")
# parking_lot = Room("Parking Lot", None, R19A)

# R19A.north + parking_lot

# Option 2 - Se tall at once, modify controller
R19A = Room("Mr. Weibe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, "R19A")


living_room = Room("Living Room",  "The TV is Screeching on the North wall " 
                                   "while a distant dog barks. \n" 
                                   "The front door is leading to Northeast. \n" 
                                   "The hallway is leading to the East. \n",
                   'tv', 'hallway', 'couch', 'window', 'front_yard', None, 'hallway', None)
tv = Room("Tv", "Its ear piercing. \n", None, 'living_room', 'couch', 'window', 'front_yard',
          None, 'hallway', None)
hallway = Room("The hallway", "A narrow hallway with family photos arranged "
                              "across the wall. \n"
                              "The kitchens to the East.\n"
                              "A room is to the West. \n ",
               'living_room', 'kitchen', 'backyard', 'room1', None, None, None,  None)
couch = Room("The Couch", "good for taking long naps on",
             'tv', 'hallway', None, 'window', 'front_yard', None, 'hallway', None)
window = Room("The Window", "can't see much. \n"
                            "doesn't look like anybody is out today. \n",
              None, 'living_room', None, None, 'front_yard', None,
              'hallway', None)
front_yard = Room("The Front Yard", "The really is no one out here. \n"
                                    "The whole neighborhood looks condemned. \n",
                  'grass', 'car', 'living_room', None, 'road', 'road1', None, None)
grass = Room("The Grass", "", 'road_1', 'my_car', 'front_yard', None, 'road_1', 'road_1',
             None, None)
road_1 = Room("The Road", "Maybe if i follow this road East "
                          "I could get somewhere. \n"
                          "If only i had a car.", None, 'nroad', 'grass', None, None,
              None, "my_car", "grass")
kitchen = Room("The Kitchen", "The kitchen", 'garage', 'stake_knives', None, 'hallway', None,
               None, None, None)
my_car = Room("Empty Drive-Way", "", 'road', 'bushes', 'front_yard', 'front_yard', 'nroad',
              'road1', None, 'front_yard')
bushes = Room("Some bushes", "I can see my neighbors nice car from here",
              'road', None, None, "my_car", 'nroad', 'road1', None, 'front_yard')
garage = Room("The Garage", "Nothing here besides a tool box to the west. \n",
              None, None, 'kitchen', 'tool_box', None, None, None, None)
tool_box = Room("Toolbox", "There is tape and a wrench in here. \n",
                None, 'garage', None, None, None, None, None, None)
backyard = Room("The Backyard", "There is a broken open fence to my neighbors yard in the east. \n"
                                "I think im going crazy is that barking?. \n",
                'hallway', 'almost_otherside', 'fence1', 'garden', 'wall1',
                'wall1', 'fence1', 'fence1')
garden = Room("A garden", "If only there was time to stop and smell the roses agin. \n",
              'wall1', 'back_yard', 'fence1', 'fence1', 'hallway',
              None, 'fence1', None)
fence1 = Room("Fence", "", 'backyard', 'almost_otherside', None, 'backyard', 'backyard',
              'backyard', None, None)
wall1 = Room("Wall", "", 'north', 'backyard', 'fence1', 'backyard', 'backyard',
             'backyard', 'backyard', 'backyard')
almost_otherside = Room("An Open Fence", "Okay the growling is definitely more prevalent. \n"
                                         "If i continue to go this way that dog is gonna attack me. \n",
                        'wall1', 'dog', 'fence1', 'dog', None, 'hallway', None, 'backyard')
fence2 = Room("Fence", "", 'dog', 'dog', 'south', 'backyard', 'backyard',
              'backyard', None, None)
dog = Room("Neighbors Backyard",  "", 'nlr', 'pool', 'fence2', 'almost_otherside', 'wall2',
           'wall2', 'fence2', 'fence2')
wall2 = Room("wall", "", None, 'backyard', 'fence2', 'backyard', None,
             None, 'backyard', 'backyard')
nlr = Room("Neighbor Living Room", "There is a kitchen to the Northwest. \n"
                                   "and a hallway to the east ", 'ntv', 'nhw', 'dog', 'nwindow', 'nhw',
           'nkitchen', None, None)
nkitchen = Room("Kitchen", "The outside front door is to the Northeast. \n"
                           "There are keys on the North counter!", 'counter1', 'nhw', 'counter', 'nwindow', 'ndoor',
                'ngarage', 'nhw', 'nlr')
nhw = Room("Hallway", "A hallway with one door to the North wall and"
                      "one door to the South wall. ", 'room2', None, 'room3', 'nlr', None,
           None, None, None)
ndoor = Room("Neighbor's portch", " ", 'grass2', 'offlawn', 'nkitchen', 'ncar', 'nroad',
             'noroad', 'southeast', 'southwest')
nroad = Room("The Road", " ", None, 'playgrounds', 'grass2', 'nroad', None,
             "road1", 'grass2', 'ncar')
ncar = Room("Neighbor's Car", " ", 'north', 'east', 'south', 'west', 'nroad',
            'nroad', 'grass1', None)
grass2 = Room("The Neigbor's Lawn", " ", 'nroad', 'nroad', 'ndoor', 'ncar', 'nroad',
              'noroad', None, None)
playgrounds = Room("Playground Front Gate", " ", None, 'east', 'south', 'nroad', 'northeast',
                   'northwest', 'southeast', 'southwest')
nkitchen.item = "key"


player = Player("You", living_room)

playing = True
directions = ['north', 'east', 'south', 'west', 'northeast', 'northwest',
              'southeast', 'southwest', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
            print()
    elif "pick up" in command:
        item_name = command[8:].lower()
        if item_name == player.current_location.item:
            print("You pick up the %s" % player.current_location.item)
            player.inventory.append(player.current_location.item)
            if item_name == "keycard":
                living_room.north = "secret"
    else:
        print("Command Not Found")

print()
