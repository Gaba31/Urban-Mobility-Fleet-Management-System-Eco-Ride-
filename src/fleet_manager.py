from vehicle import ElectricCar , ElectricScooter

class FleetManager:
    def __init__(self):
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name in self.hubs:
            print(f"Hub '{hub_name}' already exists")
        else:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' does not exist")
            return

        if vehicle in self.hubs[hub_name]:
            print("Vehicle with this ID already exists in the hub")
            return

        self.hubs[hub_name].append(vehicle)
        print(f"Vehicle added to hub '{hub_name}'")

    def get_vehicles_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])

    def search_vehicles_by_battery(self,min_battery=80):
        all_vehicles = []

        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)

        return list(
            filter(lambda v: v.battery_percentage > min_battery, all_vehicles)
        )

    def get_vehicle_by_type(self):

        categorized = {
            "ElectricCar": [],
            "ElectricScooter": []
        }

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                if isinstance(vehicle, ElectricCar):
                    categorized["ElectricCar"].append(vehicle)
                elif isinstance(vehicle, ElectricScooter):
                    categorized["ElectricScooter"].append(vehicle)

        return categorized