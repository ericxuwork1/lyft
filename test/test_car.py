import unittest
from datetime import datetime
from battery.spindler_battery import SpindlderBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine



class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        car = SpindlderBattery(current_date, last_service_date)
        self.assertTrue(car.need_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        car = SpindlderBattery(current_date, last_service_date)
        self.assertFalse(car.need_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        car = SpindlderBattery(current_date, last_service_date)
        self.assertTrue(car.need_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        car = SpindlderBattery(current_date, last_service_date)
        self.assertFalse(car.need_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        car = SpindlderBattery(current_date, last_service_date)
        self.assertTrue(car.need_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        car = SpindlderBattery(current_date, last_service_date)
        self.assertFalse(car.need_service())
        

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.need_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        car = SternmanEngine(warning_light_is_on)
        self.assertFalse(car.need_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        car = NubbinBattery(current_date, last_service_date)
        self.assertTrue(car.need_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        car = NubbinBattery(current_date, last_service_date)
        self.assertFalse(car.need_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        car = NubbinBattery(current_date, last_service_date)
        self.assertTrue(car.need_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        car = NubbinBattery(current_date, last_service_date)
        self.assertFalse(car.need_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.need_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.need_service())


if __name__ == '__main__':
    unittest.main()
