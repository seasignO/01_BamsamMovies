from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('send_message/', views.send_message, name='send_message'),
    path('my_message/', views.my_message, name='my_message')
]
