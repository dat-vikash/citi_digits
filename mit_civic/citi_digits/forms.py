__author__ = 'vikashdat'

from django import forms
from django.contrib.localflavor.us.forms import USStateField
from django.contrib.localflavor.us.us_states import STATE_CHOICES


class SignUpForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'input-small'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'input-small'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    schoolName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School Name'}))
    schoolAddress = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School Address'}))
    schoolCity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City','class':'input-small'}))
    schoolState = USStateField(widget=forms.Select(
        choices=STATE_CHOICES,attrs={'placeholder':'State', 'class':'input-small'}))
    className = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Class Name'}))
