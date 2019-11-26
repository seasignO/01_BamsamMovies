# -*- coding: utf-8 -*-
from pprint import pprint
import json
import requests
from copy import deepcopy
with open('movies.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
key = '8cd57daba319f543423d53955a196f8c'
actors = []
movies = []
for idx, data in enumerate(json_data.get("results")):
    # pprint(data)
    movie_id = json_data['results'][idx]['id']
    url = 'https://api.themoviedb.org/3/movie/'
    url_detail = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={key}&language=ko-KR'
    details = requests.get(url_detail).json()
    movie = {}
    actor = {}
    fields = {}
    fields_a = {}
    movie["pk"] = idx+1
    movie["model"] = "movies.movie"
    fields["title"] = data.get("title")
    if data['poster_path']:
        fields["poster_path"] = data.get("poster_path")
    if data['backdrop_path']:
        fields["backdrop_path"] = data.get("backdrop_path")
    fields["overview"] = data.get("overview")
    fields["vote_average"] = data.get("vote_average")
    fields["popularity"] = data.get("popularity")
    fields["original_title"] = data.get("original_title")
    fields["release_date"] = data.get("release_date")
    fields["runtime"] = details.get("runtime")
    genres = []
    for i in range(len(data.get('genre_ids'))):
       genres.append(data['genre_ids'][i]) 
    fields["genres"] = genres
    url += f'{ data["id"] }/credits?api_key={key}'
    res = requests.get(url)
    res = res.json()
    # pprint(res)
    a={}
    b = []
    crews = res.get('crew')
    director = []
    for j in range(0, len(crews)):
        if crews[j]['job'] == 'Director':
            director.append(crews[j]['name'])
    fields['director'] = director[0]
    for i in range(len(res.get('cast'))):
        if i > 4: break
        actor['pk'] = (idx*5)+i+1
        actor['model'] = 'movies.actor'
        if res.get('cast')[i].get('profile_path'):
            a['tmbd_actor_id'] = res.get('cast')[i].get('id')
            a['name'] = res.get('cast')[i].get('name')
            a['character'] = res.get('cast')[i].get('character')
            a['profile_path'] = res.get('cast')[i].get('profile_path')
        actor['fields'] = a
        k = deepcopy(actor)
        actors.append(k)
        b.append((idx*5)+i+1)
    fields["actors"] = b
    movie["fields"] = fields
    movies.append(movie)