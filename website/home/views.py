from django.http import HttpRequest
from .forms import PlaytestEmailSignUpForm, PressMessageForm


def handel_playtest_request(request: HttpRequest):
    if request.method == "POST":
        playtest_form = PlaytestEmailSignUpForm(request.POST)
        press_form = PressMessageForm(request.POST)
        if playtest_form.is_valid():
            playtest_form.save(commit=True)
        if press_form.is_valid():
            print(press_form.cleaned_data)
