import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
       self.room = Room("Diamond_lounge")
       self.guest = Guest("kelly")
       self.song = Song("Joleen", "Dolly Parton")
       

    def test_room_has_name(self):
        self.assertEqual("Diamond_lounge", self.room.name)

    def test_add_guest_to_room(self):
        room = Room("Diamond_lounge")
        self.room.add_guest(room)
        self.assertEqual("kelly", self.guest.name)


    def test_remove_guest_from_room(self):
        room = Room("Diamond_lounge")
        self.room.add_guest(room)
        self.room.remove_guest(room)
        self.assertEqual("Diamond_lounge", self.room.name)

    def test_add_song_to_room(self):
        song = Song("Joleen", "Dolly Parton")
        self.room.add_song(song)
        self.assertEqual("Joleen", self.song.name)

    