# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Training, Activity, Sport, Method, Intensity

# Create your views here.
def trainings(request):
    trainings = Training.objects.all()
    activities = Activity.objects.all()
    return render(request, 'trainings.html', {'trainings': trainings, 'activities': activities})