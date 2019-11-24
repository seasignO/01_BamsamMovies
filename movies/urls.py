from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('genre_page/', views.genre_page, name='genre_page')
]
