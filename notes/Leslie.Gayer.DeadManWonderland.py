world_map = {
    'LIVING_ROOM': {
        'NAME': "Living Room",
        'DESCRIPTION': " That couch inst very comfortable.\n"
                       "The TV is Screeching on the North wall "
                       "while a distant dog barks. \n" 
                       "The front door is leading to Northeast. \n" 
                       "The kitchen door is leading to the East. \n"
                       "And the hallway to the Southeast\n",
        'PATHS': {
             'NORTH': "TV",
             'NORTHEAST': "FRONT_YARD",
             'EAST': "HALLWAY",
             'SOUTHEAST': "HALLWAY",
             'SOUTH': "COUCH",
             'WEST': 'WINDOW'

        }
    },

    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "Theres a kitchen that looks well taken care of \n"
                       "with stake knives hanging above the oven to the East. "
                       "and door to the garage is to the North. \n"
                       "I wonder whats in the fridge. ",
        'PATHS': {
                'NORTH': "GARAGE",
                'WEST': "HALLWAY",
                'EAST': "STAKE_KNIVES"
        }
    },

    'FRONT_YARD': {
        'NAME': "Porch",
        'DESCRIPTION': "Theres nobody out here,\n"
                       "It looks like everybody left.\n"
                       "to the East is my car. Wait. MY CAR IS GONE\n"
                       "Isn't that convenient\n",
        'PATHS': {
             'NORTH': "ROAD",
             'NORTHEAST': "ROAD",
             'EAST': "MY_CAR",
             'NORTHWEST': "ROAD",
             'SOUTH': "LIVING_ROOM"
        }
    },

    'TV': {
        'NAME': "Tv",
        'DESCRIPTION': "The tv is loud and screeching\n" 
                       "The front door is leading to Northeast. \n" 
                       "The kitchen door is leading to the East. \n",
        'PATHS': {
             'NORTHEAST': "FRONT_YARD",
             'EAST': "KITCHEN",
             'SOUTHEAST': "HALLWAY",
             'SOUTH': "COUCH",
             'WEST': "WINDOW"
         }
    },

    'HALLWAY': {
        'NAME': "Hallway",
        'DESCRIPTION': "A narrow hallway with family photos arranged on the wall\n" 
                       "The kitchen is to the Northeast\n" 
                       "A door to a room is to the West\n",
        'PATHS': {
             'NORTH': "LIVING_ROOM",
             'NORTHEAST': "KITCHEN",
             'EAST': "KITCHEN",
             'WEST': "ROOM1",
             'SOUTH': "BACKYARD"
        }
    },

    'MY_CAR': {
        'NAME': "Drive Way",
        'DESCRIPTION': "My very empty drive way\n" 
                       "Who could have wanted my broken down car that bad\n" 
                       "My neighbors car is brand new\n",
        'PATHS': {
             'NORTH': "ROAD",
             'NORTHEAST': "ROAD",
             'NORTHWEST': "ROAD",
             'EAST': "BUSHES",
             'SOUTHWEST': "FRONT_YARD",
             'SOUTH': "FRONT_YARD"
        }
    },

    'BUSHES': {
        'NAME': "Bushes",
        'DESCRIPTION': "This has a nice view of my neighbors car\n",
        'PATHS': {
             'NORTH': "ROAD",
             'NORTHEAST': "ROAD",
             'NORTHWEST': "ROAD",
             'EAST': "I cant go through rose bushes",
             'SOUTHWEST': "FRONT_YARD"
        }
    },

    'GARAGE': {
        'NAME': "The Garage",
        'DESCRIPTION': "An partially empty space with a toolbox and the left\n",
        'PATHS': {
             'EAST': "KITCHEN",
             'WEST': "TOOLBOX",
             'SOUTH': "KITCHEN"
        }
    },

    'BACKYARD': {
        'NAME': "The Backyard",
        'DESCRIPTION': "A small backyard with a garden full of lilies\n" 
                       "The fence is open to the East\n" 
                       "The barking isn't faint anymore\n",
        'PATHS': {
             'NORTH': "HALLWAY",
             'EAST': "ALMOST_OTHERSIDE",
             'WEST': "GARDEN",
             'SOUTH': "FENCE"
        }
    },

    'ALMOST_OTHERSIDE': {
        'NAME': "Fence",
        'DESCRIPTION': "The neighbors dog is staring rather aggressively " 
                       "for my liking\n" 
                       "If im gonna go further i should have an offering\n",
        'PATHS': {
             'NORTHWEST': "HALLWAY",
             'EAST': "DOG",
             'WEST': "BACKYARD",
             'SOUTH': "FENCE",
             'NORTH': "FENCE"
        }
    },
    'COUCH': {
        'NAME': "Couch",
        'DESCRIPTION': "Just a couch\n",
        'PATHS': {
            'NORTHWEST': "WALL",
            'EAST': "KITCHEN",
            'WEST': "WINDOW",
            'NORTH': "TV"
        }
    },
    'NEIGHBORS_BACKYARD': {
        'NAME': "Neighbors backyard",
        'DESCRIPTION': "Im right infront of the golden retreiver? \n"
                       "What should i do? \n",
        'PATHS': {
            'NORTHWEST': "WALL",
            'EAST': "POOL",
            'WEST': "ALMOST_OTHERSIDE",
            'SOUTH': "FENCE",
            'NORTH': "NSL"
        }
    },
    'NLR': {
        'NAME': "Neigbors living room",
        'DESCRIPTION': "Another blaring tv\n"
                       "The kitchen is to the Northwest\n"
                       "A hallway is to the Northeast\n",
        'PATHS': {
            'NORTHWEST': "NKITCHEN",
            'EAST': "SIDEWALL",
            'WEST': "WALL",
            'SOUTH': "NEIGHBORS_BACKYARD",
            'NORTH': "NTV"
        }
    },
    'NKITCHEN': {
        'NAME': "Neighbors Kitchen",
        'DESCRIPTION': "Another blaring tv\n"
                       "The kitchen is to the Northwest\n"
                       "A hallway is to the Northeast\n",
        'PATHS': {
            'NORTHWEST': "NGARAGE",
            'EAST': "NCOUNTER",
            'WEST': "WALL",
            'SOUTH': "WALL",
            'NORTH': "COUNTER",
            'NORTHEAST': "NEIGHBORS_DOOR"
        }
    },
    'WINDOW': {
        'NAME': "Window",
        'DESCRIPTION': "A window showing the side of my neighbors house\n",
        'PATHS': {
            'NORTHWEST': "WALL",
            'EAST': "KITCHEN",
            'SOUTH': "COUCH",
            'NORTH': "TV",
            'NORTHEAST': "FRONT_YARD"
        }
    },
    'ROAD': {
        'NAME': "Road",
        'DESCRIPTION': "An open road going west to east\n",
        'PATHS': {
            'SOUTHWEST': "FRONT_YARD",
            'SOUTH': "LIVING_ROOM",
            'SOUTHEAST': "MY_CAR"
        }
    }



}

# Controller

playing = True
current_node = world_map["LIVING_ROOM"]
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'NORTHWEST',
              'SOUTHWEST',  'NORTHEAST', 'SOUTHEAST']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't got that way")
    else:
        print("Command Not Found")

    print()
