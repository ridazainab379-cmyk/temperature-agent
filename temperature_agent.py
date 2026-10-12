
room_temperatures = {
    "Room1": "Cold",
    "Room2": "Normal"
}

heater_on_count = {
    "Room1": 0,
    "Room2": 0
}


def temperature_agent(room, temperature):
    room_temperatures[room] = temperature

    if temperature == "Cold":
        heater_on_count[room] += 1
        return "Turn Heater ON"

    elif temperature == "Hot":
        return "Turn Heater OFF"

    elif temperature == "Normal":
        if all(temp == "Normal" for temp in room_temperatures.values()):
            return "All Rooms Comfortable - Idle"
        else:
            return "Move to Other Room to Check"

    else:
        return "Unknown Temperature"


print("Room\tTemperature\tAction")

readings = [
    ("Room1", "Cold"),
    ("Room2", "Normal"),
    ("Room1", "Normal"),
    ("Room2", "Hot"),
    ("Room2", "Normal")
]

for room, temperature in readings:
    action = temperature_agent(room, temperature)
    print(f"{room}\t{temperature}\t\t{action}")

print("\nHeater ON Count:")
for room, count in heater_on_count.items():
    print(f"{room}: {count}")
