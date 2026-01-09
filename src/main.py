from vehicle import *
from fleet_manager import FleetManager


class EcoRideMain:

    @staticmethod
    def display_menu():
        print("\n====== Eco-Ride Urban Mobility System ======")
        print("1. Add Fleet Hub")
        print("2. Add Vehicle to Hub")
        print("3. View Vehicles by Hub")
        print("4. Search Vehicles (Battery > 80%)")
        print("5. View Vehicles by Type")
        print("6. Fleet Analytics (Vehicle Status Count)")
        print("7. Sort Vehicles in Hub by Model (A-Z)")
        print("8. Exit")

    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")
        fleet_manager = FleetManager()

        while True:
            EcoRideMain.display_menu()
            choice = input("Enter your choice (1-8): ").strip()

            # This one is for adding hub
            if choice == "1":
                hub_name = input("Enter hub name: ").strip()
                fleet_manager.add_hub(hub_name)

            # This one is for adding vehicle to hub
            elif choice == "2":
                hub_name = input("Enter hub name: ").strip()

                print("\nVehicle Types:")
                print("1. Electric Car")
                print("2. Electric Scooter")
                vehicle_choice = input("Select vehicle type (1/2): ").strip()

                vehicle_id = input("Enter Vehicle ID: ").strip()
                model = input("Enter Model Name: ").strip()

                try:
                    battery = int(input("Enter Battery Percentage: "))
                except ValueError:
                    print("Battery percentage must be a number")
                    continue

                if vehicle_choice == "1":
                    try:
                        seating_capacity = int(input("Enter Seating Capacity: "))
                        vehicle = ElectricCar(vehicle_id, model, battery, seating_capacity)
                        fleet_manager.add_vehicle_to_hub(hub_name, vehicle)
                    except ValueError:
                        print("Seating capacity must be a number")

                elif vehicle_choice == "2":
                    try:
                        max_speed_limit = int(input("Enter Max Speed Limit: "))
                        vehicle = ElectricScooter(vehicle_id, model, battery, max_speed_limit)
                        fleet_manager.add_vehicle_to_hub(hub_name, vehicle)
                    except ValueError:
                        print("Speed limit must be a number")

                else:
                    print("Invalid vehicle selection")


            elif choice == "3":
                hub_name = input("Enter hub name: ").strip()
                vehicles = fleet_manager.get_vehicles_by_hub(hub_name)

                if not vehicles:
                    print("No vehicles found or hub does not exist")
                else:
                    print(f"\nVehicles in '{hub_name}' Hub:")
                    for v in vehicles:
                        print(f"- ID: {v.vehicle_id}, Model: {v.model}, Battery: {v.battery_percentage}%")

            elif choice == "4":
                try:
                    min_battery = int(input("Enter minimum battery percentage: "))
                except ValueError:
                    print("Battery percentage must be a number")
                    continue

                results = fleet_manager.search_vehicles_by_battery(min_battery)

                if not results:
                    print("No vehicles found with battery above given percentage")
                else:
                    print("\nVehicles with high battery:")
                    for v in results:
                        print(f"- ID: {v.vehicle_id}, Model: {v.model}, Battery: {v.battery_percentage}%")


            elif choice == "5":
                categorized = fleet_manager.get_vehicles_by_type()

                print("\n--- Electric Cars ---")
                if not categorized["ElectricCar"]:
                    print("No Electric Cars found")
                else:
                    for v in categorized["ElectricCar"]:
                        print(f"- ID: {v.vehicle_id}, Model: {v.model}, Battery: {v.battery_percentage}%")

                print("\n--- Electric Scooters ---")
                if not categorized["ElectricScooter"]:
                    print("No Electric Scooters found")
                else:
                    for v in categorized["ElectricScooter"]:
                        print(f"- ID: {v.vehicle_id}, Model: {v.model}, Battery: {v.battery_percentage}%")

            elif choice == "6":
                summary = fleet_manager.fleet_status_summary

                print("\n--- Fleet Status Summary ---")
                for status, count in summary.items():
                    print(f"{status}: {count}")

            elif choice == "7":
                hub_name = input("Enter hub name: ").strip()
                sorted_vehicles = fleet_manager.sort_vehicles_by_model(hub_name)

                if not sorted_vehicles:
                    print("No vehicles to display")
                else:
                    print(f"\nVehicles in '{hub_name}' (Sorted by Model):")
                    for v in sorted_vehicles:
                        print(v)
            # Exit
            elif choice == "8":
                print("Thank you for using Eco-Ride")
                break

            else:
                print("Invalid choice. Please select between 1 and 8.")


if __name__ == "__main__":
    EcoRideMain.main()
