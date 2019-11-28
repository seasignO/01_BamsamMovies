from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from .forms import CustomUserCreationForm, MessageForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Message, Movie
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
    user_messages = Message.objects.filter(receive=user)
    # followings = user.followings.all()
    context = {'user': user, 'userMessages': user_messages, }
    return render(request, 'accounts/messages.html', context)

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)   
        # form.receive = request.POST.get('receive')
        receive_user = get_object_or_404(get_user_model(), pk=request.POST.get('receive'))
        form.receive = receive_user
        # form.comment = request.POST.get('comment')
        print(request.POST.get('comment'))
        # form.movie = request.POST.get('movie') if request.POST.get('movie') else ' '
        print(form)
        # print(form)
        if form.is_valid():
            print('유효성 통과')
            t_form = form.save(commit=False)
            t_form.send = request.user
            t_form.is_read = False
            t_form.save()
    return redirect('accounts:my_message')


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

@login_required
def read_message(request, message_pk):
    if request.is_ajax():
        message = get_object_or_404(Message, pk=message_pk)
        if message.is_read == False:
            message.is_read = True
        context = {}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest  

@login_required
def manage_choice(request):
    if request.user.is_staff:
        users = get_user_model().objects.all()
        movies = Movie.objects.all()
        context = {'users': users, 'movies': movies}
        return render(request, 'accounts/manage_choice.html', context)
    else:
        return redirect('movies:main')

@login_required
def user_modify(request, user_pk):
    if not request.user.is_staff:
        return redirect('movies:main')
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:manage_choice')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = { 'form': form }
    return render(request, 'accounts/user_modify.html', context)

    
