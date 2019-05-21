import random


def fight(player_list: list, enemy_list: list):
    # print()
    # print("FIGHT MODE INITIATED")
    print()
    # Player fights person
    player_index = 0
    # enemy_index = -1
    enemy_index = 0
    while player in player_list and len(enemy_list) > 0:
        enemy_list_names = []
        for name in range(len(enemy_list)):
            enemy_list_names.append(enemy_list[name].name)
        print("Of your enemies, there is", ", ".join(enemy_list_names))
        attacking = input("Who do you want to attack?")
        target = None
        for enemy in range(len(enemy_list)):
            if enemy_list[enemy].name.lower() in attacking.lower():
                target = enemy_list[enemy]
        if target is not None:
            print("You fight %s" % target.name)
            try:
                print(target.dialogue[3])
            except IndexError:
                print("This is an angry one. Too angry to speak coherently.")
            # print(player_list)  # DEV THINGY
            # print(enemy_list)  # DEV THINGY
            # print(enemy_index)  # DEV THINGY
            player_list[player_index].attack(target)
            if target.health <= 0:
                enemy_list.remove(target)
        if len(enemy_list) > 1:  # IF MULTIPLE ENEMIES
            enemy_index += 1
        if enemy_index > len(enemy_list) - 1:
            enemy_index = 0

        # Enemy fights player
        if len(enemy_list) > 0:
            print()
            print("You're attacked")
            # print(enemy_list)  # DEV THINGY
            # print(enemy_index)  # DEV THINGY
            target = random.choice(player_list)
            enemy_list[enemy_index].attack(target)
            if target.health <= 0:
                player_list.remove(target)
        else:
            print("All the enemies are dead")
            print()

        player_index += 1
        if player_index > len(player_list) - 1:
            player_index = 0

        if player.health <= 0:
            print("You have died")
            quit(0)
            return


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
    def __init__(self,  name,  energy_amount=None):
        super(Food, self).__init__(name)
        self.energy_amount = energy_amount

    def replenish_energy(self):
        Character.energy = Character.energy + self.energy_amount


class Junk(Food):
    def __init__(self):
        super(Junk, self).__init__('Junk Food', 25)


class Cans(Food):
    def __init__(self):
        super(Cans, self).__init__('Canned Food', 50)


steak = Food(10)


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Gun(Weapon):
    def __init__(self,  name, damage):
        super(Gun, self).__init__(name, damage)
        self.dmg_type = "gun"


class Fists(Weapon):
    def __init__(self):
        super(Fists, self).__init__("Fists", 10)
        self.dmg_type = "knife"


class Pistol(Gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", 50)
        self.dmg_type = "gun"


class Shotgun(Gun):
    def __init__(self):
        super(Shotgun, self).__init__("Shotgun", 100)
        self.dmg_type = "gun"


class Knife(Weapon):
    def __init__(self, name, damage):
        super(Knife, self).__init__(name, damage)
        self.dmg_type = "knife"


class KitchenKnife(Knife):
    def __init__(self):
        super(KitchenKnife, self).__init__('Kitchen Knife', 50)
        self.dmg_type = "knife"


class HuntingKnife(Knife):
    def __init__(self):
        super(HuntingKnife, self).__init__('Hunting Knife', 35)
        self.dmg_type = "knife"


class Melee(Weapon):
    def __init__(self, name, damage):
        super(Melee, self).__init__(name, damage)
        self.dmg_type = "knife"


class Katana(Melee):
    def __init__(self):
        super(Katana, self).__init__('Katana', 40)
        self.dmg_type = "knife"


class Machete(Melee):
    def __init__(self):
        super(Machete, self).__init__('Basic Machete', 23)
        self.dmg_type = "knife"


class Bat(Weapon):
    def __init__(self, name, damage, knockout=False):
        super(Bat, self).__init__(name, damage)
        self.knockout = knockout
        self.dmg_type = "bat"


class Woodbat(Bat):
    def __init__(self):
        super(Woodbat, self).__init__('Woodbat', 50)
        self.dmg_type = "bat"

    def hit_target(self, origin, target):
        hit = random.randint(0, 100)
        if hit > 50:
            origin.knockout = True
            target.take_damage(self.damage)
            target.awake = False
            print("%s knocked them out and %s received 50 damage" % (origin.name, target.name))
        else:
            origin.knockout = False
            target.take_damage(self.damage)
            print("They received 50 damage")


class Ironbat(Bat):
    def __init__(self):
        super(Ironbat, self).__init__('Ironbat', 65)
        self.dmg_type = "bat"

    def hit_target(self, origin, target):
        hit = random.randint(0, 100)
        if hit > 40:
            origin.knockout = True
            target.take_damage(self.damage)
            target.awake = False
            print("%s knocked them out and %s received 50 damage" % (origin.name, target.name))
        else:
            origin.knockout = False
            target.take_damage(self.damage)
            print("They received 50 damage")


class Armor(Item):
    def __init__(self, name, protectiong, protectionk, protectionb):
        super(Armor, self).__init__(name)
        self.protectiong = protectiong
        self.protectionk = protectionk
        self.protectionb = protectionb


class GenericArmor(Armor):
    def __init__(self):
        super(GenericArmor, self).__init__("Generic Armor", 0, 0, 0)


class BV(Armor):
    def __init__(self):
        super(BV, self).__init__("Bulletproof Vest", 100, 0, 0)


class RG(Armor):
    def __init__(self):
        super(RG, self).__init__("Riot Gear", 80, 50, 100)


class LJ(Armor):
    def __init__(self):
        super(LJ, self).__init__("Leather Jacket", 0, 9, 20)


class Key(Item):
    def __init__(self, name):
        super(Key, self).__init__(name)


key1 = Key("key")


class Medicine(Item):
    def __init__(self, name, heal_amount=None):
        super(Medicine, self).__init__(name)
        self.heal_amount = heal_amount

    def heal(self):
        player.health = player.health + self.heal_amount


excedrin = Medicine("Excedrin", 20)


class BBA(Armor):
    def __init__(self):
        super(BBA, self).__init__("Basic Body Armor", 0, 25, 25)


class Room(object):
    def __init__(self, name,  description, north=None,  east=None, south=None,
                 west=None, northeast=None, northwest=None,  southeast=None,
                 southwest=None, characters=None, items=None):
        if characters is None:
            characters = []
        if items is None:
            items = []
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
        self.characters = characters
        self.items = items


class Character(object):
    def __init__(self, name, dialogue, starting_location, health=100, weapon=Fists(),
                 armor=GenericArmor(), ):
        self.name = name
        self.dialogue = dialogue
        self.dialogue_line = 0
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.dead = False
        self.awake = True
        self.bitten = False
        self.inventory = []
        # self.follower = None  # Character Object
        self.provoked = False
        self.spotted = False
        self.greeted = False
        self.current_location = starting_location
        self.followers = []

    def die(self):
        print("Death has come upon %s" % self.name)
        for p in range(len(self.inventory)):
            self.current_location.items.append(self.inventory[p])
        if self.weapon is not None or not isinstance(self.weapon, Fists):
            self.current_location.items.append(self.weapon)
        if self.armor is not None:
            self.current_location.items.append(self.armor)
        self.current_location.characters.remove(self)

    def take_damage(self, damage: int, damage_type):
        if self.armor is None:
            self.health -= damage
        else:
            if damage_type == "gun":
                if self.armor.protectiong > damage:
                    print("No damage is done because of great armor")
                else:
                    self.health -= damage - self.armor.protectiong
            elif damage_type == 'knife':
                if self.armor.protectionk > damage:
                    print("No damage is done because of great armor")
                else:
                    self.health -= damage - self.armor.protectionk
            elif damage_type == 'bat':
                if self.armor.protectionb > damage:
                    print("No damage is done because of great armor")
                else:
                    self.health -= damage - self.armor.protectionb
        print("%s have/has %d health left" % (self.name, self.health))
        print()
        if self.health <= 0:
            self.die()

    def attack(self, target):
        # if self.weapon is None:
        #
        # print(self.weapon.damage)
        print("%s attacked %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage, self.weapon.dmg_type)
        print()

    def move(self, new_location):
        """ This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        if new_location is None:
            print("Uh...")
            return
        if len(self.followers) > 0:
            for friend in range(len(self.followers)):
                self.followers[friend].current_location.characters.remove(self.followers[friend])
            new_location.characters.append(self.followers[friend])

        self.current_location = new_location

    def find_next_room(self, direction):
        """
        This method  searches the current room so see if a room
        exists in that direction
        :param direction: The direction you want to move to
        :return: The room object if it exists, or none if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        if name_of_room == "ncar" and key1 not in self.inventory and isinstance(self, Player):
            print("You don't have the keys")
            return None
        elif name_of_room == "ncar" and key1 in self.inventory and isinstance(self, Player):
            print("You have the keys to your neighbors' car! Yay!")
        return globals()[name_of_room]


# class Animal(Character):
#     def __init__(self, name, health=100, ):
#         super(Animal, self).__init__(name, health)


Dog = Character("Buster", "", 'dog', 10)


class Player(Character):
    def __init__(self, name, starting_location, energy=100, health=100,
                 weapon=Fists(), armor=GenericArmor()):
        """

        :type weapon: weapon
        """
        super(Player, self).__init__(name, None, starting_location, health, weapon, armor)
        self.current_location = starting_location
        self.energy = energy
        self.inventory = []

    def die(self):
        print("You have died" % self.name)
        for i in range(len(self.inventory)):
            self.current_location.items.append(self.inventory[i])
        if self.weapon is not None or not isinstance(self.weapon, Fists):
            self.current_location.items.append(self.weapon)
        if self.armor is not None:
            self.current_location.items.append(self.armor)
        print("Now you're dead. You can't do anything when you're dead.")
        quit(0)


class NPC(Character):
    def __init__(self, name, dialogue, starting_location, health=100, weapon=Fists(),
                 armor=GenericArmor()):
        super(NPC, self).__init__(name, dialogue, starting_location, health, weapon, armor)


class Enemy(Character):
    def __init__(self, name, dialogue, starting_location, health=75, weapon=Fists(), armor=GenericArmor()):
        super(Enemy, self).__init__(name, dialogue, starting_location, health, weapon, armor)


class Zombie(Character):
    def __init__(self, name, dialogue, health, starting_location, weapon=Fists(), armor=None):
        super(Zombie, self).__init__(name, dialogue, starting_location, health, weapon, armor)
        self.bite = False


"""'Dean', 'Maverick', 'Asher', 'Westly', 'Hunter', 'Misty',
                          'Naomi', 'Demitres', 'Kodak'"""


# I = Player("")
Dean = Character("Dean", ["Hello?", "what do you want", "Do you need something?",
                          "You wanna get tough huh? then lets go!", "Take this",
                          "WAIT!, Is it okay if i can hitch a ride?", "Thanks you're a doll",
                          "No?, NO?, you're going to regret that"], 'tv', 5, Machete(), LJ())


# Sam = Character("Sam", ["Hey!", "Whats up!", "How are you doing?", "You want to fight?, Really?, okay then"],
#                 100, Pistol(), RG())
#
# Maverick = Character("Maverick", ["Go away", "I dont have time for this", "Stop bothering me",
#                                   "You're gonna regret that"], 50, 10, None)
# Ash = Character("Ash", "", 100, Ironbat(), RG())
#
# Misty = NPC("Misty", ["The whole world has gone to hell so quickly in the last couple days.",
#             "Who knew the dead would rise. ME! that's who!", "I'LL KILL EVERY LAST ONE OF THEM!",
#                       "You have underestimated me"], 80, Shotgun(), BV())

Zombie1 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40, None)
Zombie1.provoked = True
# Zombie2 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie2.provoked = True
# Zombie3 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie3.provoked = True
# Zombie4 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie4.provoked = True
# Zombie5 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie5.provoked = True
# Zombie6 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie6.provoked = True
# Zombie7 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie7.provoked = True
# Zombie8 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie8.provoked = True
# Zombie9 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie9.provoked = True
# Zombie10 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie10.provoked = True
# Zombie11 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie11.provoked = True
# Zombie12 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie12.provoked = True
# Zombie13 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie13.provoked = True
# Zombie14 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie14.provoked = True
# Zombie15 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie15.provoked = True
# Zombie16 = Zombie("Zombie", ["errrhggg", "Ghrrr", "uhhhg", "ERRRRRGGH"], 40)
# Zombie16.provoked = True


# Option 1 - define as we go
# R19A = Room("Mr. Weibe's Room")
# parking_lot = Room("Parking Lot", None, R19A)

# R19A.north + parking_lot

# Option 2 - Se tall at once, modify controller
"""R19A = Room("Mr. Weibe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, "R19A")"""


living_room = Room("Living Room",  "The TV is Screeching on the North wall " 
                                   "while a distant dog barks. \n" 
                                   "The front door is leading to Northeast. \n" 
                                   "The hallway is leading to the East. \n",
                   'tv', 'hallway', 'couch', 'stree', 'front_yard', None, 'hallway', None)
tv = Room("Tv", "Its ear piercing. \n", None, 'living_room', 'couch', 'window', 'front_yard',
          None, 'hallway', None, [Dean, Zombie1], [key1])
Zombie1.current_location = tv
hallway = Room("The hallway", "A narrow hallway with family photos arranged "
                              "across the wall. \n"
                              "The kitchens to the East.\n"
                              "A room is to the West. \n ",
               'living_room', 'kitchen', 'backyard', 'room1', None, None, None,  None)
room1 = Room("Room", "My dresser is to the North. \n"
                     "my bed is to the West and my closet "
                     "is to the South",
             'dresser', 'hallway', 'closet', 'bed', 'r1w', 'r1w', 'r1w', 'r1w')
dresser = Room("dresser", "", None, 'hallway', 'closet',
               'r1w', None, None, 'r1w', 'bed', None)
bed = Room("Bed", "", 'r1w', 'hallway', 'r1w', None, 'dresser', None,
           'closet', None)
r1w = Room("Wall", "", 'room1', 'room1', 'room1', 'room1', 'room1', 'room1', 'room1',
           'room1', 'room1')
closet = Room("Closet", 'Some thin shirts and sweaters with a leather jacket', 'dresser',
              'r1w', None, 'r1w', 'r1w', 'bed', 'r1w', None, None, [LJ()])
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
road_1 = Room("The Road", "Maybe if i follow this road East"
                          "I could get somewhere.\n", None, 'nroad', 'grass', None, None,
              None, "my_car", "grass")
kitchen = Room("The Kitchen", "There is a couple raw steaks to the east \n"
                              "with a bloody knife to the side", 'garage', 'kitchen_knives', None, 'hallway', None,
               None, None, None, None)
kitchen_knives = Room("A kitchen knife and stake", "", 'garage', None, None, 'hallway',
                      None, None, None, None, None, [KitchenKnife()])
my_car = Room("Empty Drive-Way", "", 'road', 'bushes', 'front_yard', 'front_yard', 'nroad',
              'road1', None, 'front_yard')
bushes = Room("Some bushes", "I can see my neighbors nice car from here",
              'road', None, None, "my_car", 'nroad', 'road1', None, 'front_yard')
garage = Room("The Garage", "Nothing here besides a tool box to the west. \n",
              None, None, 'kitchen', 'tool_box', None, None, None, None)
tool_box = Room("Toolbox", "There is tape and a wrench in here. \n",
                None, 'garage', None, None, None, None, None, None, None)
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
                        'wall1', 'dog', 'fence1', 'backyard', None, 'hallway', None, 'backyard')
fence2 = Room("Fence", "", 'dog', 'dog', 'south', 'backyard', 'backyard',
              'backyard', None, None)
dog = Room("Neighbors Backyard", "", 'nlr', 'pool', 'fence2', 'almost_otherside', 'wall2',
           'wall2', 'fence2', 'fence2', [Dog])
dog.current_location = 'dog'
friendly = Room("Buster is right here", 'nlr', 'pool', 'fence2', 'almost_otherside', 'wall2', 'wall2', 'fence2',
                'fence2', [Dog])
wall2 = Room("wall", "", None, 'backyard', 'fence2', 'backyard', None,
             None, 'backyard', 'backyard')
nlr = Room("Neighbor Living Room", "There is a kitchen to the Northwest. \n"
                                   "and a hallway to the east ", 'ntv', 'nhw', 'dog', 'nwindow', 'nhw',
           'nkitchen', None, None)
nkitchen = Room("Kitchen", "The front door is to the Northeast. \n"
                           "There are keys on the South counter!", 'counter1', 'nhw', 'ncounter', 'nwindow', 'ndoor',
                'ngarage', 'nhw', 'nlr')
ncounter = Room("Keys", "Some car keys. \n"
                        "Should i pick them up?", 'counter1', 'nhw', None, 'nwindow', 'ndoor',
                'ngarage', 'nhw', 'nlr', None)
nhw = Room("Hallway", "A hallway with one door to the North wall and"
                      "one door to the South wall. ", 'room2', None, 'room3', 'nlr', None,
           None, None, None)
ndoor = Room("Neighbor's portch", " ", 'grass2', 'offlawn', 'nkitchen', 'ncar', 'nroad',
             'noroad', 'southeast', 'southwest')
nroad = Room("The Road above my neighbor's house", " ", None, 'crossroads', 'grass2', 'road_1', None,
             "road1", 'grass2', 'ncar')
ncar = Room("Neighbor's Car", " ", 'north', 'east', 'south', 'west', 'nroad',
            'nroad', 'grass1', None)
drivable = Room("In Car", "I can now go farther down east", None, 'crossroads1', None, 'Endroad', None,
                None, None, None)
grass2 = Room("The Neigbor's Lawn", " ", 'nroad', 'nroad', 'ndoor', 'ncar', 'nroad',
              'noroad', None, None)
crossroads = Room("Nowhere", "I can't go and farther east on foot \n" 
                             "It would be best if i find a Car", None, None, None, 'nroad', None,
                  None, None, None)
crossroads1 = Room("Crossroads", "There are three long roads", 'muddy', 'longroad', 'forest', 'nroad', None, None,
                   None, None)
muddy = Room("long stretch of muddy land", "There is no way i can get through this on foot \n""i should head back",
             'dies', None, 'crossroads1', None, None, None, None, None)
die = Room("You die", "You can respawn by moving", 'living_room', 'lving_room', 'lving_room', 'lvin_room', 'iving_room')
forest = Room("Forest Entryway", "looks like a deep forest that could stretch for miles", 'crossroads1', 'nothing',
              'dforest', 'nothing', None, None, None, None)
sforest = Room("Shallow Forest", "Nothing much here besides a weird shine coming from a tree to the East", 'forest',
               'tree', 'walkers1', None, None, None, None, None)
tree = Room("Large tree", "", 'canal', 'alsh', 'stree', 'sforest', None, None,
            None, None, None, [HuntingKnife])
alsh = Room("Small Path", "Looks like a small rocky pathway to the South.\n"
                          "and a small rocky pathway to the North.", 'TP', 'lof', 'BP', 'tree', None, None, None, None)
TP = Room("Rocky Pathway", "I cant see much from here", 'frsy', 'hell', 'alsh', 'frsy', 'frsy', 'frsy')
LP = Room("Rocky Pathway", "I cant see much from here", 'frsy', 'hell', 'alsh', 'frsy', 'frsy', 'frsy')

frsy = Room("Forest", "Looks easy to get lost in.", 'TP', 'TP', 'TP', 'TP', 'TP', 'TP', 'TP', 'TP')
lof = Room("Forest", "Looks easy to get lost in.", None, 'alsh', None, None, None, None, None, None)
stree = Room("Small Hill", "I hear an ungodly amount of groaning to the south, \n"
                           "i should stay away.", 'tree', 'OSS', 'sstree', 'treez', None, None,
            None, None)
treez = Room("Forest", "Looks easy to get lost in.", None, 'stree', None, None, None, None, None, None)
sstree = Room("Walkers", "Dear god.\n"
                         "There is hundreds of them!", 'tl', 'tl', 'tl', 'tl', 'tl', 'tl', 'tl', 'tl')
tl = Room("Too late. \n"
          "There is no coming out of this", "")
walkers1 = Room("I hear a couple groaning voices going south", "", 'dforest', 'st', 'walkers', None, 'st', None, None,
                None)
walkers = Room("They see me now i have to fight", "", 'walkers1', None, None, None, None, None, None, None, [])


player = Player("You", living_room)
player.follower = None

playing = True
    
directions = ['north', 'east', 'south', 'west', 'northeast', 'northwest',
              'southeast', 'southwest']
quick_directions = ['n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw']
actions = ['hit', 'shoot', 'stab', 'run', 'hide', 'pick up', 'inventory', 'get in', 'take', 'swallow']


def character_dialogue():
    for l in range(len(player.current_location.characters)):
        player.current_location.characters[l].dialogue_line = random.randint(0, 2)
        print(" %s is right here" % player.current_location.characters[l].name)
        if not player.current_location.characters[l].greeted:
            if not player.current_location.characters[l].spotted:
                print(player.current_location.characters[l].dialogue[player.current_location.characters[l].
                      dialogue_line])
                player.current_location.characters[l].spotted = True


def weapon_description():
    for u in range(len(player.current_location.items)):
        print("The %s is right here" % player.current_location.items[u].name)


initial_meeting = False


def character_events(string, extra=None):
    characters = []
    for c in range(len(player.current_location.characters)):
        characters.append(player.current_location.characters[c])
    for c in range(len(characters)):
        if characters[c].provoked:
            characters[c].attack(player)
    if "ATTACK" in string or "FIGHT" in string or "PUNCH" in string:
        for a in range(len(characters)):
            if characters[a].name.upper() in string:
                characters[a].dialogue_line = 3
                characters[a].provoked = True
                print("You have provoked", characters[a].name)
        return True
    if "HELLO" in string or "HI" in string or "GREET" in string or "WHATS UP" in string:
        for h in range(len(characters)):
            if characters[h].name.upper() in string:
                characters[h].dialogue_line = random.randint(0, 2)  # print(list[random.randint(1, 3)])
                print(characters[h].dialogue[characters[h].dialogue_line])
                characters[h].greeted = True
        return True
    if "TALK TO" in string or "SPEAK TO" in string or "ASK" in string:
        for t in range(len(characters)):
            if characters[t].name.upper() in string:
                characters[t].dialogue_line = 3
                characters[t].provoked = True
        return True
    if player.current_location == 'crossroads1' and not extra:
        print(Dean.dialogue[5])
        answer = input(Dean.dialogue[5])
        if answer == "yes" in string:
            print(Dean.dialogue[6])
            Dean.follower = True
        if answer == "no" in string:
            print(Dean.dialogue[7])
            Dean.provoked = True
        return True
    if player.current_location == 'bed' and not extra:
        answer11 = input("Would you like to sleep")
        if answer11 == "yes" in string:
            print("Okay you sleep an hour + 20 Health")
            player.health += 20
        if answer11 == "no" in string:
            print("You dont sleep")
        return True
    if player.current_location == 'friendly' and steak in player.inventory and not extra:
        answer1 = input("Should i give Buster the steak")
        if answer1 == "no" in string:
            Dog.provoked = True
            print("The dog attacked you")
        if answer1 == "yes" in string:
            Dog.follower = True
            print("The dog is now following you")
            player.inventory.remove(steak)
        return True
    if player.current_location == 'dog' and steak not in player.inventory and not extra:
        Dog.provoked = True
        print("The dog attacked you, you have died")
        quit(0)
    return False


"""Dean.attack(Sam)
Sam.attack(Dean)"""

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    character_dialogue()
    weapon_description()
    print()
    # print("You have %d" %d (player.inventory))

    command = input(">_")

    if 'q' in command.lower() or 'quit' in command.lower() or 'exit' in command.lower():
        print(input("Are you sure you want to exit?"))
        if ['yea', 'yes', 'ya', 'ya']:
            playing = False
    elif command.lower() in directions or command.lower() in quick_directions:
        if command.lower() in quick_directions:
            pos = quick_directions.index(command.lower())
            command = directions[pos]
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
            print()
    elif 'pick up' in command.lower() or 'take' in command.lower() or 'grab' in command.lower():
        item_name = command[8:]
        for item in player.current_location.items:
            if item_name.lower() == item.name.lower():
                print("You pick up a %s" % item.name)
                print("It is now in your inventory")
                player.inventory.append(item)
                if item_name == "keycard":
                    living_room.north = "secret"
                if item == key1:
                    print("You now have the keys to your neighbor's car.")
                    grass2.west = 'drivable'
                if item == steak:
                    print("You should save this for later you might need it")
                    backyard.east = 'friendly'
    elif 'swallow' in command.lower() or 'take' in command.lower():
        item_name = command[8:]
        for item in player.current_location.items:
            if item_name.lower() == item.name.lower():
                if type(item) is Medicine:
                    item.heal()
                    print("You swallow %s" % item.name)
                    print("you now have %s" % player.health)
                    excedrin.heal()
                player.inventory.remove(item)
    elif 'talk' in command.lower() or "hi" in command.lower():
        character_events(command.upper())
    elif 'fight' in command.lower() or 'attack' in command.lower() or 'punch' in command.lower():
        # Character_name = command[6:]
        # for person in range(len(player.current_location.characters)):
        #     if Character_name.lower() == player.current_location.characters[person].name.lower():
        ques = input("You want to fight?")
        if ques == 'yes':
            character_events(command.upper())
            # players = [player]
            enemies = []
            for i in range(len(player.current_location.characters)):
                if player.current_location.characters[i].provoked:
                    enemies.append(player.current_location.characters[i])
                    print(player.current_location.characters[i].name, "ADDED TO ENEMIES")
            players = player.followers + [player]

            fight(players, enemies)
        if ques == 'no':
            print("You back down from the fight")
        character_events(command.upper())
    elif command.lower() in actions:
        if actions[5]:
            print(player.inventory)
    else:
        print("Command Not Found")
    character_events(command.upper())
    
print()
