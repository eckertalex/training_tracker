from django import forms
from django.utils.timezone import now
from .models import *

class NewTrainingForm(forms.ModelForm):
        date = forms.DateTimeField(initial=now, help_text="When did you train?", required=True)
        time = forms.IntegerField(required=True, help_text="How long did you train in minutes?")
        location = forms.CharField(max_length=45, help_text="Where did you train?")
        comment = forms.CharField(widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Type any comments in here..'}), 
            max_length=255, help_text="The max length of this field is 255.")
        description = forms.CharField(widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
            max_length=255, help_text="The max length of this field is 255.")

        class Meta:
            model = Training
            fields = ['date', 'time', 'location', 'comment', 'description']

class NewActivityForm(forms.ModelForm):
        date = forms.ModelChoiceField(queryset = Training.objects.all())
        time = forms.IntegerField(required=True, help_text="How long did you train in minutes?")
        sport_type = forms.ModelChoiceField(queryset = Sport.objects.all())
        method_type = forms.ModelChoiceField(queryset = Method.objects.all())
        intensity_type = forms.ModelChoiceField(queryset = Intensity.objects.all())

        class Meta:
            model = Activity
            fields = ['date', 'time', 'sport_type', 'method_type', 'intensity_type', ]