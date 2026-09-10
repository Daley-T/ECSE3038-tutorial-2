readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

devices = readings.copy()

def list_devices(array):
    print("Device Name" , " " , "Temperature")
    for i in range(len(array)):
        print(array[i]["name"] , " " ,array[i]["temp"])

list_devices(devices)


def avg_temp(array):
    avg:float = 0.0
    new_sum:float = 0.0
    for i in range(len(array)):
        new_sum = new_sum + devices[i]["temp"]
        avg = round((new_sum / (len(array))),2)
    print("\nAverage Temp. = " ,avg)

avg_temp(devices)


def hottest(array):
    hotter:float = 0.0
    index:int = 0
    for i in range(len(array)):
        if devices[i]["temp"] > hotter:
            hotter = devices[i]["temp"]
            index = i
    print("\nHottest Temp Dictionary:\n",devices[index])

hottest(devices)