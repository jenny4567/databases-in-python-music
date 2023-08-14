from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.albumRepository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager! \nWhat would you like to do? \n1 - List all albums \n2 - List all artists")
        choice_valid = False
        choice = input("Enter your choice: ")
        while choice_valid == False:
            if choice.isdigit():
                if int(choice) == 1:
                    album_repository = AlbumRepository(self._connection)
                    albums = album_repository.all()
                    print("Here is the list of albums:")
                    for album in albums:
                        print(f"{album.id}: {album.title}")
                    choice_valid = True
                elif int(choice) == 2:
                    artist_repository = ArtistRepository(self._connection)
                    artists = artist_repository.all()
                    print("Here is the list of artists:")
                    for artist in artists:
                        print(f"{artist.id}: {artist.name}")
                    choice_valid = True
                else:
                    print("Invalid choice (wrong number). Please choose 1 or 2: ")
                    choice = input()                    
            else:
                print("Invalid choice (not a number). Please choose 1 or 2: ")
                choice = input()

if __name__ == '__main__':
    app = Application()
    app.run()