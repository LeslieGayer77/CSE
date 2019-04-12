import random


def fight(player_list: list, enemy_list: list):
    print("You start to fight")
    print(player)
    print(player_list)
    print(enemy_list)
    # Player fights enemy/person
    player_index = 0
    enemy_index = -1
    while player in player_list and len(enemy_list) > 0:
        target = random.choice(enemy_list)
        print(target)
        player_list[player_index].attack(target)
        if target.health <= 0:
            enemy_list.remove(target)

        enemy_list += 1
        if enemy_index > len(enemy_list) - 1:
            enemy_index = 0

        # Enemy fights player
        target = random.choice(player_list)
        enemy_list[enemy_index].attack(target)

        if target.health <= 0:
            player_list.remove(target)

        player_index += 1
        if player_index > len(player_list) - 1:
            player_index = 0


class Room(object):
    def __init__(self, name,  description, north=None,  east=None, south=None,
                 west=None, northeast=None, northwest=None,  southeast=None,
                 southwest=None, characters=None, items=None, enemies1=None):
        if characters is None:
            characters = []
        if items is None:
            items = []
        if enemies1 is None:
            enemies1 = []
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
        self.enemies1 = enemies1


class Character(object):
    def __init__(self, name, dialogue, starting_location: str, health=100, resistance=75,
                 weapon=None,
                 armor=None):
        self.name = name
        self.dialogue = dialogue
        self.health = health
        self.resistance = resistance
        self.weapon = weapon
        self.armor = armor
        self.current_location = starting_location
        self.dead = False
        self.awake = True
        self.bitten = False
        self.inventory = []
        self.follower = None  # Character Object

    def take_damage(self, damage: int, damage_type):
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
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage, self.weapon.dmg_type)

    def move(self, new_location):
        """ This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        if self.follower is not None:
            self.current_location.characters.remove(self.follower)
            new_location.characters.append(self.follower)
        self.current_location = new_location

    def find_next_room(self, direction):
        """
        This method  searches the current room so see if a room
        exists in that direction
        :param direction: The direction you want to move to
        :return: The room object if it exists, or none if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        if name_of_room == "ncar" and 'Key1' not in self.inventory and isinstance(self, Player):
            print("You don't have the keys")
            return None
        return globals()[name_of_room]


class Player(Character):
    def __init__(self, name, starting_location, energy=100, health=100,
                 resistance=100, weapon=None, armor=None):
        super(Player, self).__init__(name, starting_location, starting_location,
                                     health, resistance, weapon, armor)
        self.energy = energy
        self.inventory = []


class NPC(Character):
    def __init__(self, name, dialogue, health=100, resistance=75, weapon=None,
                 armor=None):
        super(NPC, self).__init__(name, dialogue, health, resistance, weapon, armor)


class Enemy(Character):
    def __init__(self, name, dialogue, health=75, resistance=75, weapon=None, armor=None):
        super(Enemy, self).__init__(name, dialogue, health, resistance, weapon, armor)


class Zombie(Enemy):
    def __init__(self, name, dialogue, health, resistance, weapon, armor):
        super(Zombie, self).__init__(name, dialogue, health, resistance, weapon, armor)
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


class Animal(Character):
    def __init__(self, name, starting_location, health=100):
        super(Animal, self).__init__(name, health, starting_location)


Dog = Animal(input, 100)


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


class Weapon(Item):
    def __init__(self, name, damage, visibility):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.visibility = visibility


class Gun(Weapon):
    def __init__(self,  name, damage, visibility, blocked):
        super(Gun, self).__init__(name, damage, visibility)
        self.blocked = blocked
        self.dmg_type = "gun"


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
        self.dmg_type = "knife"


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
        self.dmg_type = "knife"


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
        self.dmg_type = "bat"


class Woodbat(Bat):
    def __init__(self):
        super(Woodbat, self).__init__('Woodbat', 50, 100)

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
        super(Ironbat, self).__init__('Ironbat', 65, 100)

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


class BV(Armor):
    def __init__(self):
        super(BV, self).__init__("Bulletproof Vest", 100, 0, 0)


class RG(Armor):
    def __init__(self):
        super(RG, self).__init__("Riot Gear", 80, 50, 100)


class LJ(Armor):
    def __init__(self):
        super(LJ, self).__init__("Leather Jacket", 0, 20, 20)


class Key(Item):
    def __init__(self, name):
        super(Key, self).__init__(name)


key1 = Key("Keys")


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


"""'Dean', 'Maverick', 'Asher', 'Westly', 'Hunter', 'Misty',
                          'Naomi', 'Demitres', 'Kodak'"""


Dean = Enemy("Dean", "Hello", 100, 100, Machete(1), BV())
Sam = Character("Sam", "No hablo espanol", 100, 90, 75, Pistol(), RG())
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
                   'tv', 'hallway', 'couch', 'window', 'front_yard', None, 'hallway', None)
tv = Room("Tv", "Its ear piercing. \n"
                "dean is here", None, 'living_room', 'couch', 'window', 'front_yard',
          None, 'hallway', None, None, [excedrin], [Dean])
hallway = Room("The hallway", "A narrow hallway with family photos arranged "
                              "across the wall. \n"
                              "The kitchens to the East.\n"
                              "A room is to the West. \n ",
               'living_room', 'kitchen', 'backyard', 'room1', None, None, None,  None)
room1 = Room("Room", "My dresser is to the North. \n"
                     "my bed is to the West and my closet"
                     "is to the South",
             'dresser', 'hallway', 'closet', 'bed', 'r1w', 'r1w', 'r1w', 'r1w')
dresser = Room("dresser", 'nothing in here except some Excedrin', None, 'hallway', 'closet',
               'r1w', None, None, 'r1w', 'bed', None)
bed = Room("Bed", 'should i sleep?', 'r1w', 'hallway', 'r1w', None, 'dresser', None,
           'closet', None)
r1w = Room("Wall", "", 'room1', 'room1', 'room1', 'room1', 'room1', 'room1', 'room1',
           'room1', 'room1')
closet = Room("Closet", 'Some thin shirts and sweaters with a leather jacket', 'dresser',
              'r1w', None, 'r1w', 'r1w', 'bed', 'r1w', None, None, [LJ])
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
                        'wall1', 'dog', 'fence1', 'dog', None, 'hallway', None, 'backyard')
fence2 = Room("Fence", "", 'dog', 'dog', 'south', 'backyard', 'backyard',
              'backyard', None, None)
dog = Room("Neighbors Backyard",  "There is a dog here", 'nlr', 'pool', 'fence2', 'almost_otherside', 'wall2',
           'wall2', 'fence2', 'fence2', [Dog])
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
                'ngarage', 'nhw', 'nlr', None, [key1])
nhw = Room("Hallway", "A hallway with one door to the North wall and"
                      "one door to the South wall. ", 'room2', None, 'room3', 'nlr', None,
           None, None, None)
ndoor = Room("Neighbor's portch", " ", 'grass2', 'offlawn', 'nkitchen', 'ncar', 'nroad',
             'noroad', 'southeast', 'southwest')
nroad = Room("The Road", " ", None, 'playgrounds', 'grass2', 'nroad', None,
             "road1", 'grass2', 'ncar')
ncar = Room("Neighbor's Car", " ", 'north', 'east', 'south', 'west', 'nroad',
            'nroad', 'grass1', None)
drivable = Room("In Car", "I can now go east", None, 'crossroads', None, 'Endroad', None,
                None, None, None)
grass2 = Room("The Neigbor's Lawn", " ", 'nroad', 'nroad', 'ndoor', 'ncar', 'nroad',
              'noroad', None, None)
playgrounds = Room("Nowhere", "I can't go and farther east on foot \n"
                              "It would be best if i find a vehicle", None, None, None, 'nroad', None,
                   None, None, None)


player = Player("You", living_room)
# Player.follower = Dean
player.follower = None

playing = True
directions = ['north', 'east', 'south', 'west', 'northeast', 'northwest',
              'southeast', 'southwest', 'up', 'down']
actions = ['hit', 'shoot', 'stab', 'run', 'hide', 'pick up', 'inventory', 'get in', 'take', 'swallow']


"""Dean.attack(Sam)
Sam.attack(Dean)"""

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
    elif "pick up" in command.lower():
        item_name = command[8:]
        for item in player.current_location.items:
            if item_name.lower() == item.name.lower():
                print("You pick up the %s" % item.name)
                print("It is now in your inventory")
                player.inventory.append(item)
                if item_name == "keycard":
                    living_room.north = "secret"
                if item == key1:
                    ncar = 'drivable'
    elif "swallow" in command:
        item_name = command[8:]
        for item in player.current_location.items:
            if item_name.lower() == item.name.lower():
                if type(item) is Medicine:
                    item.heal()
                    print("You swallow %s" % item.name)
                    print("you now have %s" % player.health)
                player.inventory.remove(item)
    elif "fight" in command.lower():
        Character_name = command[6:]
        for item in player.current_location.items:
            if Character_name.lower() == Character_name.lower():
                ques = input("You want to fight %s?" % Character_name)
                players = [player]
                enemies = player.current_location.characters
                if Dean in player.current_location.characters:
                    players.append(Dean)
                    enemies.remove(Dean)
                if ques == 'yes':
                    print("You fight %s" % Character_name)
                    fight(players, enemies)
                if ques == 'no':
                    print("You back down from the fight")

    elif command.lower() in actions:
        if actions[5]:
            print(player.inventory)
    else:
        print("Command Not Found")

print()
