from vehicle import ElectricCar, ElectricScooter

fleet_hubs = {}

def add_fleet_hub(location):
    if isinstance(location, str) and location.isalpha():
        location = location.title()
        if location in fleet_hubs:
            print("Location already exists")
        else:
            fleet_hubs[location] = []
            print(f"New hub added at {location}")
    else:
        raise ValueError("Invalid location name")


def add_vehicle_to_hub(location, vehicle):
    location = location.title()
    if location in fleet_hubs:
        fleet_hubs[location].append(vehicle)
        print(f"{vehicle.model} added to {location}")
    else:
        raise ValueError("Location does not exist")
