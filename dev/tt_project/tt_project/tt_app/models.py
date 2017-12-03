# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


# Create your models here.
SPORT_TYPE_CHOICES = (
    ('Strength', 'Strength'),
    ('Snow Si Skate', 'Snow Ski Skate'),
    ('Snow Ski Classic', 'Snow Ski Classic'),
    ('Roller Ski Skate', 'Roller Ski Skate'),
    ('Roller Ski Classic', 'Roller Ski Classic'),
    ('Run', 'Run'),
    ('Hike', 'Hike'),
    ('Bounding', 'Bounding'),
    ('Specific Strength', 'Specific Strength'),
)

class Sport(models.Model):
    type = models.CharField(
        max_length=45,
        choices=SPORT_TYPE_CHOICES,
        default='Run',
        primary_key=True
    )

    def __str__(self):
        return self.type

METHOD_TYPE_CHOICES = (
    ('Distance', 'Distance'),
    ('Interval', 'Interval'),
    ('Warm up', 'Warm Up'),
    ('Cool Down', 'Cool Down'),
    ('OD', 'OD'),
    ('Speed', 'Speed'),
    ('Time Trial', 'Time Trial'),
    ('Race', 'Race'),
    ('Strength', 'Strength'),
)

class Method(models.Model):
    type = models.CharField(
        max_length=45,
        choices=METHOD_TYPE_CHOICES,
        default='Distance',
        primary_key=True
    )

    def __str__(self):
        return self.type

INTENSITY_TYPE_CHOICES = (
    ('L1', 'L1'),
    ('L2', 'L2'),
    ('L3', 'L3'),
    ('L4', 'L4'),
    ('Race', 'Race'),
)

class Intensity(models.Model):
    type = models.CharField(
        max_length=45,
        choices=INTENSITY_TYPE_CHOICES,
        default='L1',
        primary_key=True
    )

    def __str__(self):
        return self.type

# Create your models here.
class Training(models.Model):
    date = models.DateTimeField(null=False)
    location = models.CharField(max_length=45)
    comment = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    athlete = models.ForeignKey(User)
    
    def __str__(self):
        return self.date.strftime('%A %d %b %Y %H:%M')
    
    def athlete_str(self):
        return self.athlete

class Activity(models.Model):
    time = models.IntegerField(null=False)
    sport_type = models.ForeignKey(Sport)
    method_type = models.ForeignKey(Method)
    intensity_type = models.ForeignKey(Intensity)
    training_id = models.ForeignKey(Training)
    training_athlete = models.ForeignKey(User)

    def __str__(self):
        return self.training_id

    def __sport__(self):
        return self.sport_type

    def __athlete__(self):
        return self.training_athlete