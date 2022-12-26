import os
import smtplib
import ssl
from email.message import EmailMessage

from django.http import HttpRequest

from .forms import PlaytestEmailSignUpForm, PressMessageForm


def handel_playtest_request(request: HttpRequest):
    if request.method == "POST":
        playtest_form = PlaytestEmailSignUpForm(request.POST)
        press_form = PressMessageForm(request.POST)
        if playtest_form.is_valid():
            playtest_form.save(commit=True)
        if press_form.is_valid():
            with smtplib.SMTP(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT'))) as smtp:
                # todo: do this in a separate thread
                smtp.starttls(context=ssl.create_default_context())
                smtp.login(os.getenv('DEFAULT_FROM_EMAIL'), os.getenv('EMAIL_PASSWORD'))
                msg = EmailMessage()
                msg.set_content(press_form.cleaned_data['message'])
                msg["Subject"] = press_form.cleaned_data["subject"]
                msg["From"] = os.getenv('DEFAULT_FROM_EMAIL')
                msg["To"] = press_form.cleaned_data['email']
                smtp.send_message(msg)
