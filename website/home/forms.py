from django import forms

from .models import PlaytestEmailSignUp


class PlaytestEmailSignUpForm(forms.ModelForm):
    class Meta:
        model = PlaytestEmailSignUp
        fields = '__all__'
