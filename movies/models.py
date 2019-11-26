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
    original_title = models.CharField(max_length=150)
    summary = models.TextField()
    poster_url = models.TextField(null=True)
    backdrop_url = models.TextField(null=True)
    teaser = models.TextField()
    come_out = models.CharField(max_length=20)
    audience = models.FloatField(null=True)
    director = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre, related_name='movies')
    # casts = models.ManyToManyField(Cast)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


    def __str__(self):
        return self.title
    
class Cast(models.Model):
    name = models.CharField(max_length=50)
    character = models.CharField(max_length=50)
    profile_path = models.TextField()
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name 

class Rating(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings_set')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    

