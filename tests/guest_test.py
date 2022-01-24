import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
            self.guest = Guest("kelly")

    def test_check_guest_names(self):
            self.assertEqual("kelly", self.guest.name)