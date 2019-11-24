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
    mes = ''
    # print('user.like_genres : ',user.like_genres.all().count())
    if user.like_genres.all().count() == 0:
        mes = '좋아하는 장르를 선택해주세요'
    else:
        mes = '이미 선호하는 장르가 있으시군요'
    context = {'mes': mes}
    return render(request, 'movies/genre_choice.html', context)


