from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name 

class Movie(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField()
    poster_url = models.TextField()
    backdrop_url = models.TextField()
    come_out = models.CharField(max_length=20)
    audience = models.IntegerField(null=True)
    character_id = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')


    def __str__(self):
        return self.title
    

class Rating(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    

