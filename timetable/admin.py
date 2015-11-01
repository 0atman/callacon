from django.contrib import admin
from django import forms
from django import template
from django.forms import TextInput
from django.contrib.admin import DateFieldListFilter

from timetable.models import Game


class AddressWithMapWidget(TextInput):
    width = 400
    height = 300
    zoom = 12

    tpl = "<br>{{% load easy_maps_tags %}}{{% easy_map address {0.width} {0.height} {0.zoom} %}}"

    def render(self, name, value, attrs=None):
        output = super(AddressWithMapWidget, self).render(name, value, attrs)

        if not value:
            return output

        t = template.Template(self.tpl.format(self))
        context = template.Context({
            'address': value,
        })
        return output + t.render(context)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    list_filter = (
        "start_time",
        "game_master",
    )
    list_display=list_filter

    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'postcode': AddressWithMapWidget({'class': 'vTextField'})
            }
