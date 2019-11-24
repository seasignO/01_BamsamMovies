from IPython import embed
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, MessageForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Message


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()

    context = {'form': form, 'isForm': 'login' }
    return render(request, 'accounts/auth_form.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')    
    else:
        form = CustomUserCreationForm()

    context = {'form': form, 'isForm': 'signup' }
    return render(request, 'accounts/auth_form.html', context)


def my_message(request):
    user = request.user
    messages = Message.objects.filter(receive=user)
    context = {'user': user, 'messages': messages}
    return render(request, 'accounts/messages.html', context)


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        # return redirect('accounts:send_message')
        if form.is_valid():
            temp = form.save(commit=False)
            temp.send = request.user
            temp.save()
            return redirect('movies:index')
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)
