from django import forms
from .models import Rating

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