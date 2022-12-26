from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import PlaytestEmailSignUp


class PlayTestEmailListing(ModelAdmin):
    model = PlaytestEmailSignUp
    menu_label = "Email List"
    menu_order = 1
    list_display = ('email',)
    search_fields = ('email',)
    list_export = ('email',)


modeladmin_register(PlayTestEmailListing)
