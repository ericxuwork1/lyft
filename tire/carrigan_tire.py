from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensor_numbers):
        self.sensor_numbers = sensor_numbers
        
        
    def need_service(self):
        number = max(self.sensor_numbers)
        return number >= 0.9