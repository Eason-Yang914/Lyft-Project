from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

import unittest
import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023,5,22)
        last_date = datetime.datetime(2019,1,1)
        battery = NubbinBattery(current_date,last_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023,5,22)
        last_date = datetime.datetime(2022,5,22)
        battery = NubbinBattery(current_date,last_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023,5,22)
        last_date = datetime.datetime(2019,1,1)
        battery = SpindlerBattery(current_date,last_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023,5,22)
        last_date = datetime.datetime(2022,5,22)
        battery = SpindlerBattery(current_date,last_date)
        self.assertFalse(battery.needs_service())
