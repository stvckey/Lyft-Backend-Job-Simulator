from car import Car

from battery.battery_type.splindler_battery import SpindlerBattery
from battery.battery_type.nubbin_battery import NubbinBattery

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine
from engine.engine_type.sternman_engine import SternmanEngine

class CarFactory:
    @staticmethod
    def build_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        car = Car(battery, engine)

        return car

    @staticmethod
    def build_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        car = Car(battery, engine)

        return car

    @staticmethod
    def build_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        car = Car(battery, engine)

        return car

    @staticmethod
    def build_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(battery, engine)

        return car

    @staticmethod
    def build_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(battery, engine)

        return car
