__author__ = 'vikashdat'

from django import forms
from django.contrib.localflavor.us.forms import USStateField
from django.contrib.localflavor.us.us_states import STATE_CHOICES


class SignUpForm(forms.Form):
    firstName = forms.CharField(initial="First Name", max_length=5)
    lastName = forms.CharField(initial="Last Name")
    password = forms.CharField(initial="Password")
    email = forms.EmailField(initial="Email")
    schoolName = forms.CharField(initial="School Name")
    schoolAddress = forms.CharField(initial="School Address")
    schoolCity = forms.CharField(initial="City")
    schoolState = USStateField(initial="State", widget=forms.Select(
        choices=STATE_CHOICES))
    teamName = forms.CharField(initial="Class Name")
    teams = forms.CharField()
