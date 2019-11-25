from django import forms
from .models import Rating, Movie

class RatingForm(forms.ModelForm):
    score = forms.IntegerField(
        label='평점',
        widget = forms.NumberInput(
            attrs={
                'class': 'col-2',
                'min': 1,
                'max': 10,
                    
            }
        )
    )
    class Meta:
        model = Rating
        fields = ('comment', 'score',)

class CustomRatingForm(forms.ModelForm):
    score = forms.IntegerField(
        widget = forms.NumberInput(
            attrs = {
                'width': '100px',
            } 
        )
    ),

    comment = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'width': '100%'
            }
        )
    )
    class Meta:
        model = Rating
        fields = ('comment', 'score')

class MovieModifyForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'