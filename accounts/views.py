from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.nethod == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')
