from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from .forms import CustomUserCreationForm, MessageForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Message
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view

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
    return redirect('accounts:login')

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

@login_required
def my_message(request):
    user = request.user
    messages = Message.objects.filter(receive=user)
    context = {'user': user, 'messages': messages}
    return render(request, 'accounts/messages.html', context)

@login_required
def send_message(request):
    if request.method == 'POST':
        receive = request.POST.get('receive')
        send = request.POST.get('send')
        content = request.POST.get('content')
        movie = request.POST.get('movie') if request.POST.get('movie') else ' '
        form = MessageForm()
        form.receive = receive
        form.send = send
        form.content = content
        form.movie = movie
        form.is_read = False
        if form.is_valid():
            form.save()

    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)

def read_message(request, message_pk):
    message = get_object_or_404(Message, pk=message_pk)
    if message.is_read == False:
        message.is_read = True

@login_required
def user_detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    context = {'user': user}
    return render(request, 'accounts/user_detail.html', context)

@login_required 
def follow(request, user_pk):
    if request.is_ajax():       
        user = get_object_or_404(get_user_model(), pk=user_pk)       
        if user.follow_user.filter(pk=request.user.pk).exists():           
            user.follow_user.remove(request.user)           
            isFollow = False  # 이미 좋아할 시 false 반환     
        else:
            user.follow_user.add(request.user)           
            isFollow = True  # 새로 좋아할 시 true 반환
        context = {'isFollow': isFollow, 'follower_count': user.follow_user.count(), 'following_count': user.followings.count(),}       
        return JsonResponse(context)     
    else:        
        return HttpResponseBadRequest  


    
