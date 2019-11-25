from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('genre_page/', views.genre_page, name='genre_page'),
    path('movie_detail/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('rating_create/<int:movie_pk>/', views.rating_create, name='rating_create')
]
