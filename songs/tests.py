from django.test import TestCase
from songs.models import Playlist, Artist, Album, Song

class SimpleTest(TestCase):
    def test_playlist(self):
    	pass

class SongTest(TestCase):
	def test_songinfo(self):
		playlist = Playlist(name="cool songs")
		artist = Artist(name="Josh")
		album = Album(name="Pizzaman")
		song = Song(name="King Ass", album=album, artist=artist, playlist=playlist)
		this.assertEquals("King Ass by Josh on Pizzaman", song.song_info())
