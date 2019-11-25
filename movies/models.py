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
    poster_url = models.TextField()
    backdrop_url = models.TextField()
    teaser = models.TextField()
    come_out = models.CharField(max_length=20)
    audience = models.IntegerField(null=True)
<<<<<<< HEAD
    character_id = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='movie_set')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
=======
    director = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

>>>>>>> 84e52e4c406203264725ebae89fb86d27e7365b0

    def __str__(self):
        return self.title
    

class Rating(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings_set')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    

