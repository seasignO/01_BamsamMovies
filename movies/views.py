from django.shortcuts import render, redirect
from accounts.models import Message
import csv
import requests, json
from datetime import datetime, timedelta
from decouple import config
from pprint import pprint
from .models import Movie, Genre

# Create your views here.
def index(request):
    messages = []
    if request.user.is_authenticated:
        messages = Message.objects.filter(receive=request.user)
    context = { 'messages': messages }
    return render(request, 'movies/index.html', context)

def get_movieData(request):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key=8cd57daba319f543423d53955a196f8c&primary_release_year=2017&sort_by=revenue.desc'
    api_data = requests.get(url).json()
    # pprint(api_data)
    movies = api_data.get('results')
    # pprint(movies)
    for movie in movies:
        empty_movie = Movie()
        empty_movie.title = movie.get('original_title')
        empty_movie.summary = movie.get('overview')
        empty_movie.come_out = movie.get('release_date')
        empty_movie.poster_url = 'https://image.tmdb.org/t/p/original/' + movie.get('poster_path')
        empty_movie.backdrop_url = 'https://image.tmdb.org/t/p/original/' + movie.get('backdrop_path')
        empty_movie.character_id = movie.get('id')
        get_genres = movie.get('genre_ids')

        empty_movie.save()
        for g in get_genres:
            empty_movie.genres.add(g)
    return redirect('movies:index')

def get_genreData(request):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key=8cd57daba319f543423d53955a196f8c&language=en-US'
    genre_data = requests.get(url).json()
    genres = genre_data.get('genres')
    for genre in genres:
        t_genre = Genre()
        t_genre.id = genre.get('id')
        t_genre.name = genre.get('name')
        t_genre.save()
    # print(genres)
    return redirect('movies:index')