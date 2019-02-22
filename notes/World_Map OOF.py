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

        # Option 1 - define as we go
        # R19A = Room("Mr. Weibe's Room")
        # parking_lot = Room("Parking Lot", None, R19A)

        # R19A.north + parking_lot

        # Option 2 - Se tall at once, modify controller
        # R19A = Room("Mr. Weibe's Room" 'parking_lot')
        # parking_lot = Room("Parking Lot", None, "R19A")


living_room = Room("Living Room", 'tv', 'hallway', 'couch',
                   'window', 'front_yard', None, 'hallway', None)
tv = Room("Tv", None, 'living_room', 'couch', 'window', 'front_yard',
          None, 'hallway', None)
hallway = Room("The hallway", 'living_room', 'kitchen', 'backyard',
               'room1', None, None, None, None)
couch = Room("The Couch", 'tv', 'hallway', None, 'window', 'front_yard', None,
             'hallway', None)
window = Room("The Window", None, 'living_room', None, None, 'front_yard', None,
              'hallway', None)
front_yard = Room("The Front Yard", 'grass', 'car', 'living_room', None, 'car',
                  'road', None, None)
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
dog = Room("Neighbors Backyard", 'nlr', 'east', 'south', 'west', 'northeast',
          'northwest', 'southeast', 'southwest')
wall2 = Room("wall", "", None, 'backyard', 'fence2', 'backyard', None,
          None, 'backyard', 'backyard')
tv = Room("Tv", 'north', 'east', 'south', 'west', 'northeast',
          'northwest', 'southeast', 'southwest')
TV = Room("Tv", 'north', 'east', 'south', 'west', 'northeast',
          'northwest', 'southeast', 'southwest')
TV = Room("Tv", 'north', 'east', 'south', 'west', 'northeast',
          'northwest', 'southeast', 'southwest')
TV = Room("Tv", 'north', 'east', 'south', 'west', 'northeast',
          'northwest', 'southeast', 'southwest')
