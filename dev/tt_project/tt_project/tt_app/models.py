# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


# Create your models here.
SPORT_TYPE_CHOICES = (
    ('STRENGTH', 'Strength'),
    ('SNOW_SKATE', 'Snow Ski Skate'),
    ('SNOW_CLASSIC', 'Snow Ski Classic'),
    ('ROLL_SKATE', 'Roller Ski Skate'),
    ('ROLL_CLASSIC', 'Roller Ski Classic'),
    ('RUN', 'Run'),
    ('HIKE', 'Hike'),
    ('BOUNDING', 'Bounding'),
    ('SPECIFIC_STRENGTH', 'Specific Strength'),
)

class Sport(models.Model):
    type = models.CharField(
        max_length=45,
        choices=SPORT_TYPE_CHOICES,
        default='RUN',
        primary_key=True
    )

    def __str__(self):
        return self.type

METHOD_TYPE_CHOICES = (
    ('DISTANCE', 'Distance'),
    ('INTERVAL', 'Interval'),
    ('WARM_UP', 'Warm Up'),
    ('COOL_DOWN', 'Cool Down'),
    ('OD', 'OD'),
    ('SPEED', 'Speed'),
    ('TIME_TRIAL', 'Time Trial'),
    ('RACE', 'Race'),
)

class Method(models.Model):
    type = models.CharField(
        max_length=45,
        choices=METHOD_TYPE_CHOICES,
        default='DISTANCE',
        primary_key=True
    )

    def __str__(self):
        return self.type

INTENSITY_TYPE_CHOICES = (
    ('L1', 'L1'),
    ('L2', 'L2'),
    ('L3', 'L3'),
    ('L4', 'L4'),
    ('RACE', 'RACE'),
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
    date = models.DateTimeField(null=False, unique=True)
    time = models.IntegerField(null=False)
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
    training_date = models.ForeignKey(Training, to_field='date')
    training_athlete = models.ForeignKey(User)

    def __str__(self):
        return self.training_date

    def __sport__(self):
        return self.sport_type

    def __athlete__(self):
        return self.training_athlete