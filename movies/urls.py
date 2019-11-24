from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_movieData/', views.get_movieData, name="get_movieData"),
    path('get_genreData/', views.get_genreData, name='get_genreData'),
]
