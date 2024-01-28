
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

import unittest

class TestCarrigan(unittest.TestCase):
    def test_should_be_serviced(self):

        sensor_number = [0.1, 0.2, 0.3, 0.9]

        tire = CarriganTire(sensor_number)
        self.assertTrue(tire.need_service())

    def test_should_not_be_serviced(self):

        sensor_number = [0.1, 0.2, 0.3, 0.4]

        tire = CarriganTire(sensor_number)
        self.assertFalse(tire.need_service())



class TestOctoprime(unittest.TestCase):
    def test_should_be_serviced(self):

        sensor_number = [0.9, 0.9, 0.9, 0.9]

        tire = OctoprimeTire(sensor_number)
        self.assertTrue(tire.need_service())

    def test_should_be_not_serviced(self):

        sensor_number = [0.1, 0.2, 0.3, 0.4]

        tire = OctoprimeTire(sensor_number)
        self.assertFalse(tire.need_service())

if __name__ == '__main__':
    unittest.main()