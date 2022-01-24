import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Joleen", "Dolly Parton" )

    def test_song_has_name(self):
        self.assertEqual("Joleen", self.song.name)
    
    def test_song_has_artist(self):
        self.assertEqual("Dolly Parton", self.song.artist)