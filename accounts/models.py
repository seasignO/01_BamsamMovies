from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Movie, Genre, Rating
# from django.conf import settings

# Create your models here.

class Message(models.Model):
    receive = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="send")
    send = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receive")
    # receive_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    is_read = models.BooleanField()

class User(AbstractUser):
    follow_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings", blank=True)
    messages = models.ForeignKey(Message, on_delete = models.CASCADE, null=True)
    like_genres = models.ManyToManyField(Genre, related_name="like_genre_users", blank=True)
    like_movies = models.ManyToManyField(Movie, related_name="like_movie_users", blank=True)
    ban_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)



# class Message(models.Model):
#     send_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receive_user")
#     comment = models.TextField()
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

