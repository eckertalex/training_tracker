# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, CreateView
from django.utils import timezone
from django.utils.decorators import method_decorator

from .forms import NewTrainingForm
from .models import *

# Create your views here.
@login_required
def trainings(request):
    trainings = Training.objects.all()
    activities = Activity.objects.all()
    return render(request, 'trainings.html', {'trainings': trainings, 'activities': activities,})

@login_required
def new_training(request):
    training = Training.objects.all()
    user = User.objects.first()
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

@method_decorator(login_required, name='dispatch')
class NewActivityView(CreateView):
    model = Activity
    fields = ('training_date', 'time', 'sport_type', 'method_type', 'intensity_type',)
    template_name = 'new_activity.html'
    pk_url_kwarg = 'training_pk'
    context_object_name = 'activity'

    def form_valid(self, form):
        ac = form.save(commit=False)
        ac.training_athlete = self.request.user
        ac.save()
        return redirect('trainings')