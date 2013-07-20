__author__ = 'vikashdat'

from django import forms
from django.contrib.localflavor.us.forms import USStateField
from django.contrib.localflavor.us.us_states import STATE_CHOICES


class SignUpForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'sign_up_medium'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'sign_up_medium'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','class':'sign_up_large'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','class':'sign_up_large'}))
    schoolName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School Name','class':'sign_up_large'}))
    schoolAddress = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School Address','class':'sign_up_large'}))
    schoolCity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City','class':'sign_up_medium'}))
    schoolState = USStateField(widget=forms.Select(
        choices=STATE_CHOICES,attrs={'placeholder':'State', 'class':'sign_up_medium'}))
    className = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Class Name','class':'sign_up_large'}))
