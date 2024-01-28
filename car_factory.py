
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlderBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensor_number):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlderBattery(current_date, last_service_date)
        tire = CarriganTire(sensor_number)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensor_number):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlderBattery(current_date, last_service_date)
        tire = OctoprimeTire(sensor_number)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage, sensor_number):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = SpindlderBattery(current_date, last_service_date)
        tire = CarriganTire(sensor_number)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensor_number):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(sensor_number)
        car = Car(engine, battery, tire)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensor_number):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = CarriganTire(sensor_number)
        car = Car(engine, battery, tire)
        return car