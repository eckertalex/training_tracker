# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Sport(models.Model):
    STRENGTH = 'Strength'
    SNOW_SKATE = 'Snow Ski Skate'
    SNOW_CLASSIC = 'Snow Ski Classic'
    ROLL_SKATE = 'Roller Ski Skate'
    ROLL_Classic = 'Roller Ski Classic'
    RUN = 'Run'
    HIKE = 'Hike'
    BOUNDING = 'Bounding'
    SPECIFIC_STRENGTH = 'Specific Strength'
    SPORT_TYPE_CHOICES = (
        (STRENGTH, 'Strength'),
        (SNOW_SKATE, 'Snow Ski Skate'),
        (SNOW_CLASSIC, 'Snow Ski Classic'),
        (ROLL_SKATE, 'Roller Ski Skate'),
        (ROLL_Classic, 'Roller Ski Classic'),
        (RUN, 'Run'),
        (HIKE, 'Hike'),
        (BOUNDING, 'Bounding'),
        (SPECIFIC_STRENGTH, 'Specific Strength'),
    )
    type = models.CharField(
        max_length=45,
        choices=SPORT_TYPE_CHOICES,
        default=RUN,
        primary_key=True
    )

    def __str__(self):
        return self.type

class Method(models.Model):
    DISTANCE = 'Distance'
    INTERVAL = 'Interval'
    WARM_UP = 'Warm Up'
    COOL_DOWN = 'Cool Down'
    OD = 'OD'
    SPEED = 'Speed'
    TIME_TRIAL = 'Time Trial'
    RACE = 'Race'
    METHOD_TYPE_CHOICES = (
        (DISTANCE, 'Distance'),
        (INTERVAL, 'Interval'),
        (WARM_UP, 'Warm Up'),
        (COOL_DOWN, 'Cool Down'),
        (OD, 'OD'),
        (SPEED, 'Speed'),
        (TIME_TRIAL, 'Time Trial'),
        (RACE, 'Race'),
    )
    type = models.CharField(
        max_length=45,
        choices=METHOD_TYPE_CHOICES,
        default=DISTANCE,
        primary_key=True
    )

    def __str__(self):
        return self.type

class Intensity(models.Model):
    L1 = 'L1'
    L2 = 'L2'
    L3 = 'L3'
    L4 = 'L4'
    RACE = 'RACE'
    INTENSITY_TYPE_CHOICES = (
        (L1, 'L1'),
        (L2, 'L2'),
        (L3, 'L3'),
        (L4, 'L4'),
        (RACE, 'RACE'),
    )
    type = models.CharField(
        max_length=45,
        choices=INTENSITY_TYPE_CHOICES,
        default=L1,
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
        return self.description

class Activity(models.Model):
    time = models.IntegerField(null=False)
    sport_type = models.ForeignKey(Sport)
    method_type = models.ForeignKey(Method)
    intensity_type = models.ForeignKey(Intensity)
    training_date = models.ForeignKey(Training, to_field='date')
    training_athlete = models.ForeignKey(User)
