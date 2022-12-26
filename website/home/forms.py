from django import forms

from .models import PlaytestEmailSignUp


class PlaytestEmailSignUpForm(forms.ModelForm):
    class Meta:
        model = PlaytestEmailSignUp
        fields = '__all__'


class PressMessageForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
