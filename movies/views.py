from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Message
import csv
import requests, json
from datetime import datetime, timedelta
from decouple import config
from pprint import pprint
from .models import Movie, Genre, Rating
import random
from .forms import RatingForm
from django.http import HttpResponse



# Create your views here.
def index(request):
    user_movies = []
    # if request.user.is_authenticated:
    #     user_movies = Movie.objects.
    messages = []
    if request.user.is_authenticated:
        messages = Message.objects.filter(receive=request.user)
    context = { 'messages': messages, 'user_movies': user_movies }
    return render(request, 'movies/index.html', context)

def genre_page(request):
    user = request.user
    # print('user.like_genres : ',user.like_genres.all().count())
    if user.like_genres.all().count() == 0:
        mes = False
    else:
        mes = True
    print(type(Movie.objects.all()))
    random_movies = random.sample(list(Movie.objects.all()), 10)
    
    context = {'mes': mes, 'random_movies': random_movies}
    return render(request, 'movies/genre_choice.html', context)

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = RatingForm()
    ratings = movie.ratings_set.all()
    print(ratings)
    context = {'movie': movie, 'form': form, 'ratings': ratings}
    return render(request, 'movies/movie_detail.html', context)

def rating_create(request, movie_pk):
    if request.is_ajax():
        movie = get_object_or_404(Movie, pk=movie_pk)
        
        pass
    else:
        pass
    # if request.method == 'POST':
    #     rating = Rating()
    #     rating.comment = request.POST.get('comment')
    #     rating.score = request.POST.get('score')
    #     rating.user = request.user
    #     rating.movie = movie
    #     rating.save()
    #     return HttpResponse('리뷰 작성 완료')

