readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

device = readings.copy()

def list_devices(array):
    print("\nDevice Name" , " " , "Temperature")
    for i in range(len(array)):
        print(array[i]["name"] , " " ,array[i]["temp"])

list_devices(device)


def avg_temp(array):
    avg:float = 0.0
    new_sum:float = 0.0
    for i in range(len(array)):
        new_sum = new_sum + device[i]["temp"]
        avg = round((new_sum / (len(array))),2)
    print("\nAverage Temp. = " ,avg)

avg_temp(device)


def hottest(array):
    hotter:float = 0.0
    index:int = 0
    for i in range(len(array)):
        if device[i]["temp"] > hotter:
            hotter = device[i]["temp"]
            index = i
    print("\nHottest Temp Dictionary:\n",device[index])

hottest(device)


def to_status(array):
    print("\nSearch device:")
    dev_srch = input()
    index:int = (len(array))+1

    for i in range (len(array)):
        if device[i]["name"] == dev_srch:
            index = i
    if(index == (len(array))+1):
        print("Device not found")

    new_dict =  {"device":(array[index]["name"]) , "status":(array[index]["online"]), "celsius":(array[index]["temp"])}
    if array[index]["online"] == True:
        new_dict |= {"status":"ok"}
    else:
        new_dict |= {"status":"offline"}

    print(new_dict)
    
to_status(device)


def by_room(array):
    print("\nDevices by room:")

    room_sort = {}
    for i in range(len(array)):
        for rooms in device:
            room = array[i]["room"]
            name = array[i]["name"]

        if room not in room_sort:
            room_sort[room] = [name]
        else:
            room_sort[room].append(name)

    print(room_sort)

by_room(device) 