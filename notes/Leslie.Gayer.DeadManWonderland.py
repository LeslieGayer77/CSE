world_map = {
    'R19A': {
        'NAME': "Home",
        'DESCRIPTION': "wake up on your couch in an uncomfortable position."
                                  "The TV is creeching on the North wall while a distant dog barks"
                                  "The front door is leading to Northeast"
                                  "The kitchen door is leading to the East",
        'PATHS': {
             'NORTH': "Tv",
             'NORTHEAST': "Front Door",
             'EAST': "Kitchen"

        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here.",
        'PATHS': {
                'SOUTH': 'R19A'
        }
    }
}



#Controller
playing = True
current_node = world_map["Home"]
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