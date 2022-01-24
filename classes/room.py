class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []
        


    def add_guest(self, room):
        self.guests.append(room)

    def remove_guest(self, room):
        self.guests.remove(room)

    def add_song(self, song):
        self.songs.append(song)

    

    
    
 

       