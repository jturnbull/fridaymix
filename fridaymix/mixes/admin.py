import datetime
from django import forms
from django.contrib import admin
from models import *


class MixAdmin(admin.ModelAdmin):
    list_display = ('title', 'start','length_display')
    search_fields = ('title','slug',)
    date_hierarchy = 'start'

admin.site.register(Mix, MixAdmin)
admin.site.register(Track)