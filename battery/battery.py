from abc import ABC, abstractmethod

from car import Car

class Battery(Car, ABC):
    @abstractmethod
    def battery_need_service(self):
        pass
