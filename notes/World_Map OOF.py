class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self. south = south
        self.east = east
        self.west = west

        # Option 1 - define as we go
        R19A = Room("Mr. Weibe's Room")
        parking_lot = Room("Parking Lot", None, R19A)

        R19A.north + parking_lot

        # Option 2 - Se tall at once, modify controller
        R19A = Room("Mr. Weibe's Room" 'parking_lot')
        parking_lot = Room("Parking Lot", None, "R19A")