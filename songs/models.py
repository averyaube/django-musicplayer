from django.db import models

class Playlist(models.Model):
	"""A playlist which should contain songs"""
	name = models.CharField(max_length=128)

class Artist(models.Model):
	"""An artist of a song"""
	name = models.CharField(max_length=128)
	description = models.TextField()

class Album(models.Model):
	"""An album that probably contains songs"""
	name = models.CharField(max_length=128)
	art = models.ImageField(upload_to='albumart/')

class Song(models.Model):
	"""A song to be played"""
	playlist = models.ForeignKey(Playlist)
	name = models.CharField(max_length=128)
	artist = models.ForeignKey(Artist)
	album = models.ForeignKey(Album)
	song_file = models.FileField(upload_to='songs/')

	def song_info(self):
		"""Return a line with the song title, artist and album"""
		return "%(ti)s by %(ar)s on %(al)s" % \
				{"ti": self.name, "ar": self.artist.name, "al": self.album.name}