from django.conf import settings

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

class LoginForm(forms.Form):
    CHOICES = (('STUDENT', 'Student',), ('TEACHER', 'Teacher',))
    role = forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'Student','class':'sign_up_medium styled-select'}),choices=CHOICES)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name or Email','class':'sign_up_large'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','class':'sign_up_large'}))


class PlayerInterviewForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput())
    buyLotteryTickets = forms.ChoiceField(widget=forms.RadioSelect(),choices=(('1','Yes'),('0','No')))
    whyOrWhyNot = forms.FileField()
    wonLottery = forms.ChoiceField(widget=forms.RadioSelect(),choices=(('1','Yes'),('0','No')),required=False)
    mostWonAmount = forms.CharField(widget=forms.TextInput(),required=False)
    averageSpentOnLotteryPerWeek = forms.CharField(widget=forms.TextInput())
    wonJackpotQuestion = forms.FileField()
    photo = forms.ImageField()
    location = forms.CharField(widget=forms.TextInput(),required=False)
    latitude = forms.CharField(widget=forms.HiddenInput(),required=False,initial=0)
    longitude = forms.CharField(widget=forms.HiddenInput(),required=False,initial=0)


