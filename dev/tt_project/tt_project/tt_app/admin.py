# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class TrainingAdmin(admin.ModelAdmin):
    list_display = ['date', 'athlete']

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['__str__', '__sport__', '__athlete__']

admin.site.register(Training, TrainingAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Sport)
admin.site.register(Method)
admin.site.register(Intensity)