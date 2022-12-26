import os
import smtplib
import ssl
from email.message import EmailMessage

from django.http import HttpRequest
from django.core.mail import send_mail

from .forms import PlaytestEmailSignUpForm, PressMessageForm


def handel_playtest_request(request: HttpRequest):
    if request.method == "POST":
        playtest_form = PlaytestEmailSignUpForm(request.POST)
        press_form = PressMessageForm(request.POST)
        if playtest_form.is_valid():
            playtest_form.save(commit=True)
        if press_form.is_valid():
            send_mail(
                press_form.cleaned_data['subject'] + f"| {press_form.cleaned_data['email']}",
                message=f"Message from {press_form.cleaned_data['email']}\n\n" + press_form.cleaned_data['message'],
                from_email=os.getenv('DEFAULT_FROM_EMAIL'),
                recipient_list=[os.getenv('DEFAULT_TO_EMAIL')]
            )

            # with smtplib.SMTP(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT'))) as smtp: # todo: do this in a
            #  separate thread smtp.starttls(context=ssl.create_default_context()) smtp.login(os.getenv(
            #  'DEFAULT_FROM_EMAIL'), os.getenv('EMAIL_PASSWORD')) msg = EmailMessage() msg.set_content(f"Message
            #  from {press_form.cleaned_data['email']}\n" + press_form.cleaned_data['message']) msg["Subject"] =
            #  press_form.cleaned_data["subject"] + f' | {press_form.cleaned_data["email"]}' msg["From"] = os.getenv(
            #  'DEFAULT_FROM_EMAIL') msg["To"] = os.getenv('DEFAULT_TO_EMAIL') smtp.send_message(msg)
