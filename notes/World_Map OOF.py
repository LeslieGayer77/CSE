class Room(object):
    def __init__(self, name,  description, north=None,  east=None, south=None,
                 west=None, northeast=None, northwest=None,  southeast=None,  southwest=None):
        self.name = name
        self.description = description
        self.north = north
        self. east = south
        self.south = east
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
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
        return globals()[name_of_room]


# Option 1 - define as we go
# R19A = Room("Mr. Weibe's Room")
# parking_lot = Room("Parking Lot", None, R19A)

# R19A.north + parking_lot

# Option 2 - Se tall at once, modify controller
R19A = Room("Mr. Weibe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, "R19A")


living_room = Room("Living Room",  "", 'tv', 'hallway', 'couch',
                   'window', 'front_yard', None, 'hallway', None)
tv = Room("Tv", "", None, 'living_room', 'couch', 'window', 'front_yard',
          None, 'hallway', None)
hallway = Room("The hallway", "", 'living_room', 'kitchen', 'backyard',
               'room1', None, None, None,  None)
couch = Room("The Couch", "", 'tv', 'hallway', None, 'window', 'front_yard', None,
             'hallway', None)
window = Room("The Window", "", None, 'living_room', None, None, 'front_yard', None,
              'hallway', None)
front_yard = Room("The Front Yard", "", 'grass', 'car', 'living_room', None, 'road',
                  'road1', None, None)
grass = Room("The Grass", "", 'road', 'my_car', 'front_yard', None, 'road1', 'road',
             None, None)
road_1 = Room("The Front Yard", "", 'grass', 'car', 'living_room', None, 'road',
              'road1', None, None)
kitchen = Room("The Kitchen", 'garage', 'stake_knives', None, 'hallway', None,
               None, None, None)
my_car = Room("Empty Drive-Way", 'road', 'bushes', 'front_yard', 'front_yard', 'road',
              'road', None, 'front_yard')
bushes = Room("Some bushes", 'road', None, None, "my_car", 'road',
              'road', None, 'front_yard')
garage = Room("The Garage", None, None, 'kitchen', 'tool_box', None,
              None, None, None)
backyard = Room("The Backyard", 'hallway', 'almost_otherside', 'fence1', 'garden', 'wall1',
                'wall1', 'fence1', 'fence1')
fence1 = Room("Fence", "Just the Fence", 'backyard', 'backyard', None, 'backyard', 'backyard',
              'backyard', None, None)
wall1 = Room("Wall", "The wall of my  house", 'north', 'backyard', 'fence1', 'backyard', 'backyard',
             'backyard', 'backyard', 'backyard')
almost_otherside = Room("Open Fence", 'wall1', 'dog', 'fence1', 'dog', None,
                        'hallway', None, 'backyard')
fence2 = Room("Fence", "Just the Fence", 'dog', 'dog', 'south', 'backyard', 'backyard',
              'backyard', None, None)
dog = Room("Neighbors Backyard",  "", 'nlr', 'pool', 'fence2', 'almost_otherside', 'wall2',
           'wall2', 'fence2', 'fence2')
wall2 = Room("wall", "", None, 'backyard', 'fence2', 'backyard', None,
             None, 'backyard', 'backyard')
nlr = Room("Neighbor Living Room", " ", 'ntv', 'nhw', 'dog', 'nwindow', 'nhw',
           'nkitchen', None, None)
nkitchen = Room("Kitchen", " ", 'counter1', 'nhw', 'counter', 'nwindow', 'ndoor',
                'ngarage', 'nhw', 'nlr')
nhw = Room("Hallway", "A hallway with one door to the North wall and"
                      "one door to the South wall. ", 'room2', None, 'room3', 'nlr', None,
           None, None, None)
ndoor = Room("Neighbor's portch", " ", 'grass2', 'offlawn', 'nkitchen', 'ncar', 'nroad',
             'noroad', 'southeast', 'southwest')
nroad = Room("The Road", " ", None, 'playground', 'ndoor', 'ncar', None,
             None, 'grass2', 'ndoor')
grass2 = Room("The Grass", " ", 'nroad', 'nroad', 'ndoor', 'ncar', 'nroad',
              'noroad', None, None)
TV = Room("Tv", " ", 'north', 'east', 'south', 'west', 'northeast',
          'northwest', 'southeast', 'southwest')
# TV = Room("Tv", " ", 'north', 'east', 'south', 'west', 'northeast',
#           'northwest', 'southeast', 'southwest')

player = Player(living_room)

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
            print("I can't got that way")
    else:
        print("Command Not Found")
