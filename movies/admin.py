from django.contrib import admin
from .models import Genre, Movie, Rating

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'summary', 'poster_url', 'backdrop_url', 'come_out', 'audience', 'character_id', 'genre',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'comment', 'score',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie)
admin.site.register(Rating, RatingAdmin)