
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery


    def needs_service(self):
        return self.engine.need_service() or self.battey.need_service()
