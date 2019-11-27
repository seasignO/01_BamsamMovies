from django import forms
from .models import Message
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('receive', 'comment', 'movie',)