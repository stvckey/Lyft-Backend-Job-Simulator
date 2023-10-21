import unittest

from tire.tire_type.carrigan_tire import CarriganTire
from tire.tire_type.octoprime_tire import OctoprimeTire

class TireTest(unittest.TestCase):
    def carrigan_service_test_true(self):
        tire_wear = [0.1, 0.2, 0.5, 0.4]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def carrigan_service_test_false(self):
        tire_wear = [0.1, 0.2, 0.3, 0.1]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())

    def octoprime_service_test_true(self):
        tire_wear = [0.9, 0.8, 0.8, 0.9]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def octoprime_service_teoctoprime(self):
        tire_wear = [0.3, 0.8, 0.8, 0.9]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())