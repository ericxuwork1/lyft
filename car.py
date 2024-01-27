from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery


    @abstractmethod
    def needs_service(self):
        return self.engine.need_service() or self.battey.need_service()
