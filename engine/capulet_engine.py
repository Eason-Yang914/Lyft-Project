# from abc import ABC

# from car import Car

from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.capulet_milage_need_service = 30000


    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage
