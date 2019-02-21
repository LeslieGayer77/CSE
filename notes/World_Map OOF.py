class Room(object):
    def __init__(self, name,  north=None,  east=None, south=None,  west=None,  northeast=None,
                 northwest=None,  southeast=None,  southwest=None):
        self.name = name
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
        couch = Room("The Couch", 'tv', 'hallway', None, 'window', 'front_yard',
                  None, 'hallway', None)
        window = Room("The Window", None, 'living_room', None, None, 'front_yard',
                  None, 'hallway', None)
        front_yard = Room("The Front Yard", 'grass', 'car', 'living_room', None, 'car',
                  'road', None, None)
        TV = Room("Tv", 'north', 'east', 'south', 'west', 'northeast',
                  'northwest', 'southeast', 'southwest')
        TV = Room("Tv", 'north', 'east', 'south', 'west', 'northeast',
                  'northwest', 'southeast', 'southwest')
