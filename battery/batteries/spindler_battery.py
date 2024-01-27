from abc import ABC


from car import Car


class SpindlderBattery(Car, ABC):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    @abstractmethod
    def battery_need_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < current_date