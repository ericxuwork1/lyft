from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor_numbers):
        self.sensor_numbers = sensor_numbers
        
        
    def need_service(self):
        number = sum(self.sensor_numbers)
        return number >= 3 