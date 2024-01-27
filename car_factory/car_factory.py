from abc import ABC, abstractmethod
from car import Car
from engine.engines.capulet_engine import CapuletEngine
from engine.engines.sternman_engine import SternmanEngine
from engine.engines.willoughby_engine import WilloughbyEngine
from battery.batteries.nubbin_battery import NubbinBattery
from battery.batteries.spindler_battery import SpindlderBattery

class CarFactory(Car, ABC):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = SpindlderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car