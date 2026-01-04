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
        print("Invalid location name")


def add_vehicle_to_hub(location, vehicle):
    location = location.title()
    if location in fleet_hubs:
        fleet_hubs[location].append(vehicle)
        print(f"{vehicle.model} added to {location}")
    else:
        print("Location does not exist")


def console():
    while True:
        print("\n1. Add Hub")
        print("2. Add Electric Car to Hub")
        print("3. Add Electric Scooter to Hub")
        print("4. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                hub = input("Enter hub location: ")
                add_fleet_hub(hub)

            case "2":
                hub = input("Enter hub location: ")
                car = ElectricCar(
                    int(input("Enter vehicle id: ")),
                    input("Enter model: "),
                    int(input("Enter battery percentage: ")),
                    int(input("Enter seating capacity: "))
                )
                add_vehicle_to_hub(hub, car)

            case "3":
                hub = input("Enter hub location: ")
                scooter = ElectricScooter(
                    int(input("Enter vehicle id: ")),
                    input("Enter model: "),
                    int(input("Enter battery percentage: ")),
                    int(input("Enter max speed limit: "))
                )
                add_vehicle_to_hub(hub, scooter)

            case "4":
                print("Exited")
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    console()

    print("\nFleet Summary:")
    for location, vehicles in fleet_hubs.items():
        print(f"\nHub: {location}")
        for v in vehicles:
            print(
                f"  ID: {v.vehicle_id}, "
                f"Model: {v.model}, "
                f"Battery: {v.battery_percentage}%"
            )
