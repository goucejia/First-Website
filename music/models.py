from django.db import models

# Create your models here.

class Album(models.Model) :
    artist = models.CharField (max_length = 250)
    title = models.CharField (max_length = 250)
    genre = models.CharField (max_length = 100)
    album_logo = models.CharField (max_length = 500)   #urls

    def __str__(self):
        return self.title + " - " + self.artist


class Song(models.Model) :
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 250)