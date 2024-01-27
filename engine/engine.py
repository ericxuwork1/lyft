from abc import ABC, abstractmethod
from car import Car

class Engine(Car, ABC):
    @abstractmethod
    def engine_need_service(self):
        pass
