# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, CreateView
from django.utils import timezone
from django.utils.decorators import method_decorator

from .forms import *
from .models import *

# Create your views here.
@login_required
def trainings(request):
    trainings = Training.objects.all().order_by('-date')
    activities = Activity.objects.all()
    return render(request, 'trainings.html', {'trainings': trainings, 'activities': activities,})

@login_required
def new_training(request):
    if request.method == 'POST':
        form = NewTrainingForm(request.POST)
        if form.is_valid():
            tr = form.save(commit=False)
            tr.athlete = request.user
            tr.save()
            return redirect('trainings')
    else:
        form = NewTrainingForm()
    return render(request, 'new_training.html', {'form': form})

@login_required
def delete_training(request, training_pk=None):
    tr = get_object_or_404(Training, pk=training_pk)
    tr.delete()
    return redirect('trainings')

@login_required
def delete_activity(request, activity_pk=None):
    ac = get_object_or_404(Activity, pk=activity_pk)
    ac.delete()
    return redirect('trainings')

@method_decorator(login_required, name='dispatch')
class TrainingUpdateView(UpdateView):
    model = Training
    fields = ('time', 'location', 'comment', 'description')
    template_name = 'edit_training.html'
    pk_url_kwarg = 'training_pk'
    context_object_name = 'training'

    def form_valid(self, form):
        tr = form.save(commit=False)
        tr.save()
        return redirect('trainings')

@login_required
def new_activity(request, training=None):
    if request.method == 'POST':
        form = NewActivityForm(user=request.user, data=request.POST)
        if form.is_valid():
            ac = form.save(commit=False)
            ac.training_athlete = request.user
            ac.save()
            return redirect('trainings')
    else:
        form = NewActivityForm(user=request.user)
    return render(request, 'new_activity.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ('training_date', 'time', 'sport_type', 'intensity_type', 'method_type')
    template_name = 'edit_activity.html'
    pk_url_kwarg = 'activity_pk'
    context_object_name = 'activity'

    def form_valid(self, form):
        ac = form.save(commit=False)
        ac.save()
        return redirect('trainings')