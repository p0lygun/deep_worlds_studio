from .models import HomePage, PlaytestEmailSignUp
from django.http import HttpRequest
from .forms import PlaytestEmailSignUpForm


def handel_playtest_request(request: HttpRequest):
    if request.method == "POST":
        playtest_form = PlaytestEmailSignUpForm(request.POST)
        if playtest_form.is_valid():
            playtest_form.save(commit=True)
