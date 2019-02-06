world_map = {
    'LIVING_ROOM': {
        'NAME': "Living Room",
        'DESCRIPTION': "wake up on your couch in an uncomfortable position. "
                                  "The TV is Screeching on the North wall while a distant dog barks. "
                                  "The front door is leading to Northeast. "
                                  "The kitchen door is leading to the East. ",
        'PATHS': {
             'NORTH': "Tv",
             'NORTHEAST': "FRONT_YARD",
             'EAST': "KITCHEN"

        }
    },
    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "Theres a kitchen that looks well taken care of "
                      "with stake knives hanging above the oven to the East. "
                       "and door to the garage is to the North. "
                      "I wonder whats in the fridge. ",
        'PATHS': {
                'NORTH': "The Garage"
        }
    }
    'FRONT_YARD':{
        'NAME': "Porch",
        'DESCRIPTION': "Theres nobody out here,"
                       "It looks like everybody left"
                       "to the East is my car. Wait. MY CAR IS GONE"
                        "Isn't that convenient",
        'PATHS': {
             'NORTH': "ROAD",
             'NORTHEAST': "FRONT_YARD",
             'EAST': "MY CAR"
        }
    }
    'Tv':{
        'NAME': "Tv",
        'DESCRIPTION': "The tv is loud and screeching"
                                  "The front door is leading to Northeast. "
                                  "The kitchen door is leading to the East. ",

    }
}



#Controller
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