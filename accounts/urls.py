from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('send_message/', views.send_message, name='send_message'),
    path('my_message/', views.my_message, name='my_message'),
    path('read_message/', views.read_message, name='read_message'),
    path('user_detail/<int:user_pk>/', views.user_detail, name='user_detail'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
]
