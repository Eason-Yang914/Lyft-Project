from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

import unittest

#CapuletEngine: Once every 30,000 miles
class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_miles = 90000
        last_service_miles = 0
        engine = CapuletEngine(current_miles,last_service_miles)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_miles = 60000
        last_service_miles = 56000
        engine = CapuletEngine(current_miles,last_service_miles)
        self.assertFasle(engine.needs_service())

#WilloughbyEngine: Once every 60,000 miles
class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_miles = 80000
        last_service_miles = 10000
        engine = WilloughbyEngine(current_miles,last_service_miles)

    def test_needs_service_false(self):
        current_miles = 70000
        last_service_miles = 40000
        engine = WilloughbyEngine(current_miles,last_service_miles)

#SternmanEngine: Only when the warning indicator is on
class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())