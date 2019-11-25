from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth import get_user_model
User = get_user_model()

class MovieSerializer(seializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'