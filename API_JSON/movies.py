import csv
import requests
import json
from pprint import pprint
from decouple import config

movies = []
result = []
api_key = config('API_KEY')

# Discover
# 최신 영화 60개를 result에 담기

for i in range(3):
# for i in range(1):
    
    page = i+1
    base_url = 'https://api.themoviedb.org/3/discover/movie?'
    url = base_url + f'api_key={api_key}&language=ko-KR&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}'
    
    response = requests.get(url)
    response_dict = response.json()
    
    # len(response_dict['results']) => 20개 
    for i in range(len(response_dict['results'])):
        movieId = response_dict['results'][i]['id']
        movies.append(movieId)

for i in range(len(movies)):
# for i in range(1):
    movie_id = movies[i]
    
    # model : Movie
    movie_tmp = {}
    movie_tmp['model'] = 'movies.movie'
    movie_tmp['pk'] = movies[i]
    base_url_movies = 'https://api.themoviedb.org/3/movie/'

    ## detail
    url_detail = base_url_movies + f'{movie_id}?api_key={api_key}&language=ko-KR'

    response = requests.get(url_detail)
    response_dict = response.json()

    title = response_dict["title"]
    original_title = response_dict["original_title"]
    summary = response_dict["overview"]
    poster_url = response_dict["poster_path"]
    backdrop_url = response_dict["backdrop_path"]
    come_out = response_dict["release_date"]
    audience = response_dict["popularity"] * 1000
    
    genres = []
    tmps = response_dict["genres"]
    for tmp in tmps:
        genres.append(tmp["id"])
    
    ## credits
    url_credits = base_url_movies + f'{movie_id}/credits?api_key={api_key}'
    
    response = requests.get(url_credits)
    response_dict = response.json()

    tmps = response_dict["crew"]
    director = ''

    for tmp in tmps:
        if tmp["job"] == "Director":
            director = tmp["name"]
            break

    ## videos
    base_url_video = 'https://api.themoviedb.org/3/movie/'
    url_video = base_url_video + f'{movie_id}/videos?api_key={api_key}&language=ko-KR'
    
    response = requests.get(url_video)
    response_dict = response.json()

    if response_dict["results"]:
        teaser = response_dict["results"][0]["key"]
    else:
        teaser = ""

    # ## actor
    # url_actor = f'http://api.themoviedb.org/3/movie/{movie_id}/casts?api_key={api_key}'

    # response = requests.get(url_actor)
    # response_dict = response.json
    # tmp_casts = response_dict["cast"]
    # cnt = 0
    # casts = []
    # # pprint(response_dict['cast'])
    # for cast in tmp_casts:
    #     if cnt == 5:
    #         break
    #     name = cast["name"]
    #     cnt += 1
    


    movie_tmp['fields'] = {
        'title': title,
        'original_title': original_title,
        'summary': summary,
        'poster_url': poster_url,
        'backdrop_url': backdrop_url,
        'teaser': teaser,
        'come_out': come_out,  
        'audience': audience,
        'director': director,
        'genres': genres,
    }
    result.append(movie_tmp)

with open('movies.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)