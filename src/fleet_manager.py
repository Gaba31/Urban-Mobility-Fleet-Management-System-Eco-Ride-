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
