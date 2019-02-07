world_map = {
    'LIVING_ROOM': {
        'NAME': "Living Room",
        'DESCRIPTION': " You wake up on your couch in an uncomfortable position. "
                       "The TV is Screeching on the North wall "
                       "while a distant dog barks. " 
                       "The front door is leading to Northeast. " 
                       "The kitchen door is leading to the East. "
                        "And the hallway to the Southeast",
        'PATHS': {
             'NORTH': "Tv",
             'NORTHEAST': "FRONT_YARD",
             'EAST': "KITCHEN",
             'SOUTHEAST': "HALLWAY"

        }
    },

    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "Theres a kitchen that looks well taken care of "
                       "with stake knives hanging above the oven to the East. "
                       "and door to the garage is to the North. "
                       "I wonder whats in the fridge. ",
        'PATHS': {
                'NORTH': "GARAGE",
                'WEST': "LIVING_ROOM"
        }
    },

    'FRONT_YARD': {
        'NAME': "Porch",
        'DESCRIPTION': "Theres nobody out here,"
                       "It looks like everybody left"
                       "to the East is my car. Wait. MY CAR IS GONE"
                       "Isn't that convenient",
        'PATHS': {
             'NORTH': "ROAD",
             'NORTHEAST': "ROAD",
             'EAST': "MY_CAR"
        }
    },

    'Tv': {
        'NAME': "Tv",
        'DESCRIPTION': "The tv is loud and screeching" 
                       "The front door is leading to Northeast. " 
                       "The kitchen door is leading to the East. ",
        'PATHS': {
             'NORTHEAST': "FRONT_YARD",
             'EAST': "KITCHEN",
             'SOUTHEAST': "HALLWAY"
         }
    },

    'HALLWAY': {
        'NAME': "Hallway",
        'DESCRIPTION': "A narrow hallway with family photos arranged on the wall" 
                       "The kitchen is to the Northeast" 
                       "A door to a room is to the West",
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
        'DESCRIPTION': "My very empty drive way" 
                       "Who could have wanted my broken down car that bad" 
                       "My neighbors car is brand new",
        'PATHS': {
             'NORTH': "ROAD",
             'NORTHEAST': "ROAD",
             'NORTHWEST': "ROAD",
             'EAST': "BUSHES",
             'SOUTHWEST': "FRONT_YARD"
        }
    },

    'BUSHES': {
        'NAME': "Bushes",
        'DESCRIPTION': "This has a nice view of my neighbors car",
        'PATHS': {
             'NORTH': "ROAD",
             'NORTHEAST': "ROAD",
             'NORTHWEST': "ROAD",
             'EAST': "I cant go through rose bushes",
             'SOUTHWEST': "FRONT_YARD"
        }
    }
}
print()

# Controller

playing = True
current_node = world_map["LIVING_ROOM"]
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'NORTHWEST', 'SOUTHWEST',  'NORTHEAST', 'SOUTHEAST']
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
