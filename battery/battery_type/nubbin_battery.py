import datetime
from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = datetime.datetime.now()
        self.last_service_date = last_service_date

    def needs_service(self):
        years = self.current_date.year - self.last_service_date.year
        return years > 4
