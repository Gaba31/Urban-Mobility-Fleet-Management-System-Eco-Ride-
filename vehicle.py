from abc import ABC , abstractmethod

class Vehicle(ABC):

    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = int(vehicle_id)
        self.model = str(model)
        # self.battery_percentage = None
        self.set_battery_percentage(battery_percentage)
        self.__maintenance_status = None
        self.__rental_price = None

    def set_rental_price(self,price):
        """
            Sets the rental price of the vehicle

            Parameter
            ---------
            price : int
                Rental price value

            Raises
                ValueError
                    If the rental price is less than 0
        """
        if isinstance(price,(int,float)) and price>=0:
            self.__rental_price = int(price)
        else:
            raise ValueError("Rental price cannot be negative")

    def get_rental_price(self):
        """
            This will return rental status of the vehicle.
        """
        return self.__rental_price

    def get_maintenance_status(self):
        """
            This will return maintainace status of the vehicle.
        """
        return self.__maintenance_status

    def set_maintenance_status(self, status):
        """
             Sets the maintance status of the vehicle.

             Parameters
             ----------
                status :

             Raises
             ----------

        """
        self.__maintenance_status = str(status)

    def set_battery_percentage(self,battery_percentage):
        """
              Sets the battery percentage of the vehicle.

              Parameters
              ----------
              battery_percentage : int
                  Battery percentage value

              Raises
              ------
              ValueError
                  If battery percentage is out of range
              """
        if isinstance (battery_percentage,(int,float)) and(battery_percentage >= 0 and battery_percentage<=100):
            self.battery_percentage = int(battery_percentage)
        else:
            raise ValueError("Battery Percentage must be between 0 and 100")


class ElectricCar(Vehicle):
    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity):
        super().__init__(vehicle_id,model,battery_percentage)
        self.seating_capacity = None
        self.set_seating_capacity(seating_capacity)

    def set_seating_capacity(self,seating_capacity):
        """
            Sets the seating_capacity of car

            Parameters
                seating_capacity : int

            Raises
                ValueError if the capacity is not of int type
        """
        if isinstance(seating_capacity,int):
            self.seating_capacity = seating_capacity
        else:
            raise ValueError("Seating Capacity can't be in decimal number or in a String Format")

class ElectricScooter(Vehicle):
    def __init__(self,vehicle_id, model, battery_percentage,max_speed_limit):
        super().__init__(vehicle_id,model,battery_percentage)
        self.max_speed_limit = None
        self.set_max_speed_limit(max_speed_limit)

    def set_max_speed_limit(self,max_speed_limit):
        """
            Set the speed limit for Electric Scooter

            Parameter
            -----
                max_speed_limit : int or float

            Raises
                Value Error : Value can't be -ve or greater than 130 or can't be a string
        """
        if isinstance(max_speed_limit,(int,float)) and (max_speed_limit<=130 and max_speed_limit>=0):
            self.max_speed_limit = int(max_speed_limit)
        else:
            raise ValueError("Speed limit can't be -ve or greater than 130 or can't be a string")
