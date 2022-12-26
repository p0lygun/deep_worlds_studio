from django.db import models

from wagtail.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, route
from django.template.response import TemplateResponse
from django.http import HttpRequest



class HomePage(RoutablePageMixin, Page):
    @route('^$')
    def base(self, request: HttpRequest):
        if request.method == "POST":   # pass request to view if it's a post request
            from .views import handel_playtest_request
            handel_playtest_request(request)
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )

    def get_context(self, request, *args, **kwargs):
        from .forms import PlaytestEmailSignUpForm, PressMessageForm
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['playtest_form'] = PlaytestEmailSignUpForm()
        context['press_form'] = PressMessageForm()
        return context


class PlaytestEmailSignUp(models.Model):
    email = models.EmailField(help_text="Emails of users that want to participate in playtest", null=True, unique=True)
