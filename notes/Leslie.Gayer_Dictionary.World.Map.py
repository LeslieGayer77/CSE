world_map = {
    'R19A': {
        'NAME': "Mr. Weibe's room",
        'DESCRIPTION': "The classroom you are in right now"
                                  "now. There are two doors on the North wall.",
        'PATHS': {
             'NORTH': "PARKING_LOT"
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
current_node = world_map["R19A"]
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False