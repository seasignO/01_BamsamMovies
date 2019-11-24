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

