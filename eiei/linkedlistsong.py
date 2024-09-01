class Song:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add a new song to the end of the playlist
    def add_song(self, title):
        new_song = Song(title)
        if not self.head:
            self.head = self.tail = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

    # Remove a song from the playlist
    def remove_song(self, title):
        temp = self.head
        while temp is not None:
            if temp.title == title:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                if temp == self.tail:
                    self.tail = temp.prev
                del temp
                return True
            temp = temp.next
        return False  # Song not found

    # Display all songs in the playlist
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.title)
            temp = temp.next

def main():
    my_playlist = Playlist()
    my_playlist.add_song("Song 1")
    my_playlist.add_song("Song 2")
    my_playlist.add_song("Song 3")

    print("Current Playlist:")
    my_playlist.display()

    my_playlist.remove_song("Song 2")
