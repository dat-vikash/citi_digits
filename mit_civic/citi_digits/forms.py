from django.conf import settings

__author__ = 'vikashdat'

from django import forms
from django.contrib.localflavor.us.forms import USStateField
from django.contrib.localflavor.us.us_states import STATE_CHOICES


class SignUpForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'sign_up_medium','style':'width:150px;'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'sign_up_medium','style':'width:150px;'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','class':'sign_up_large'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','class':'sign_up_large'}))
    schoolName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School Name','class':'sign_up_large'}))
    schoolAddress = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'School Address','class':'sign_up_large'}))
    schoolCity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City','class':'sign_up_medium','style':'width:150px; margin-left:-4px;'}))
    schoolState = USStateField(widget=forms.Select(
        choices=STATE_CHOICES,attrs={'placeholder':'State', 'class':'sign_up_medium','style':'width:150px;'}),initial='NY')
    className = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Class Name','class':'sign_up_large'}))

class LoginForm(forms.Form):
    CHOICES = (('STUDENT', 'Student',), ('TEACHER', 'Teacher',))
    role = forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'Student','class':'sign_up_medium styled-select','style':'width:150px;'}),choices=CHOICES)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name or Email','class':'sign_up_large'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','class':'sign_up_large'}))


class PlayerInterviewForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 100%;'}))
    buyLotteryTickets = forms.ChoiceField(widget=forms.RadioSelect(),choices=(('1','Yes'),('0','No')))
    whyOrWhyNot = forms.FileField(widget=forms.FileInput(attrs={'class':'add-media-styled-button'}))
    wonLottery = forms.ChoiceField(widget=forms.RadioSelect(),choices=(('1','Yes'),('0','No')),required=False)
    mostWonAmount = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 90%;'}),required=False)
    averageSpentOnLotteryPerWeek = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 90%;'}))
    wonJackpotQuestion = forms.FileField(widget=forms.FileInput(attrs={'class':'add-media-styled-button'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class':'add-media-styled-button'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 100%;'}),required=False)
    latitude = forms.CharField(widget=forms.HiddenInput(),required=False,initial=0)
    longitude = forms.CharField(widget=forms.HiddenInput(),required=False,initial=0)

class RetailerInterviewForm(forms.Form):
    storeName = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 100%;'}))
    sellLotteryTickets = forms.ChoiceField(widget=forms.RadioSelect(),choices=(('1','Yes'),('0','No')))
    whyOrWhyNot = forms.FileField()
    customersPerDay = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 90%;'}),required=False)
    percentageCustomers = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 89%;'}),required=False)
    amountPerVisit = forms.ChoiceField(required=False,widget=forms.RadioSelect(),choices=(('1-TICKET','1-ticket'),('2-5-TICKETS','2-5 tickets'),
                                                                             ('6-10-TICKETS','6-10 tickets'),('11-OR-MORE-TICKETS',
                                                                              '11 or more tickets')))
    goodForNeighborhoodQuestion = forms.FileField()
    photo = forms.ImageField()
    location = forms.CharField(widget=forms.TextInput(attrs={'style':'width: 100%;'}),required=False)
    latitude = forms.CharField(widget=forms.HiddenInput(),required=False,initial=0)
    longitude = forms.CharField(widget=forms.HiddenInput(),required=False,initial=0)

class TourForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'style':'width:50%'}))
    teamPhoto = forms.ImageField(required=False)

class TourSlide(forms.Form):
    image = forms.ImageField(required=True,label="Add an Image")
    isCoverPhoto = forms.BooleanField(widget=forms.CheckboxInput(),label="Use as Cover Photo",required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={"style":'width: 50%;height : 250px;'}),label="Add text")
    link =forms.CharField(widget=forms.TextInput(attrs={'style':'width:50%'}),required=False,label="Link (optional)")
    audio = forms.FileField(required=False,label="Add audio")



