class vehicle:
    def __init__(self,_vehicle_id,_base_rate):
        self._vehicle_id=_vehicle_id
        self._base_rate=_base_rate
    def display_details(self):
        return f"vehicle ID :{self._vehicle_id}, Base Rate: {self._base_rate}"
    def rental_charge(self):
        return 0.0
class car(vehicle):
    def __init__(self, _vehicle_id, _base_rate,num_seats):
        super().__init__(_vehicle_id, _base_rate)
        self.num_seats=num_seats
    def rental_charge(self):
        return self._base_rate*self.num_seats
class Bike(vehicle):
    def __init__(self, _vehicle_id, _base_rate,bike_type):
        super().__init__(_vehicle_id, _base_rate)
        self.bike_type=bike_type
    def rental_charge(self):
        return self._base_rate*0.5
    def calculate_rental(vehicle):
        return vehicle.rental_charge()
car = car("CAR001", 100.0, 4)
bike = Bike("BIKE001", 100.0, "Scooter")
print(car.display_details())
print(calculate_rental(car))
print(+bike.display_details())
print(calculate_rental(bike))


