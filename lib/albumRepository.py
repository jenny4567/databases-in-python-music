from lib.album import Album

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    # Find a single artist by their id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    # Create a new Album record
    def create(self, Album):
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s,%s)', [Album.title, Album.release_year, Album.artist_id]
        )

    # Delete an album record
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [id])