import csv
import requests, json
from datetime import datetime, timedelta
from decouple import config
from pprint import pprint
from .models import Movie

key = config('API_KEY')
targetDt = 2017

url = f'https://api.themoviedb.org/3/discover/movie?api_key={key}&primary_release_year={targetDt}&sort_by=revenue.desc'
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
    genres = movie.get('genre_ids')
    for genre in genres:
        empty_movie.genre_ids = genre
    empty_movie.save()
# pprint(result)

# #csv를 이용하여 차트를 만든다. excel view 확장자를 이용하면 더 쉽게 볼 수 있다.
# with open ('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
# fieldnames = ('movieCd', 'movieNm', 'audiAcc')
# writer = csv.DictWriter(f, fieldnames=fieldnames)
# writer.writeheader()
# for value in result.values():
#     print(value)
#     writer.writerow(value)