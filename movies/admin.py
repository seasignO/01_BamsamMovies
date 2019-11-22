from django.contrib import admin
from .models import Genre, Movie, Rating

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'summary', 'director',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'comment', 'score',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)