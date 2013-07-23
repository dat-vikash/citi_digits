import json
import django
from django.db import transaction
from django.http import HttpResponse, QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
import forms
from models import School, Teacher, Team, Student, CityDigitsUser
from service import MembershipService
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def index(request):
    """
     Loads base index
    """
    current_user = request.user
    return render_to_response('index.html', {},
                   context_instance=RequestContext(request))

@transaction.autocommit
def signUp(request):
    """
      Sign up
    """
    #Process Registration information
    if request.method == 'POST':
        #bound the form
        form  = forms.SignUpForm(request.POST)
        if form.is_valid():
            #place form data into query dict for easier access
            formData = QueryDict(request.body)
            #create entities
            school = School.objects.create(name=formData.get('schoolName'),address=formData.get('schoolAddress'),
                            city=formData.get('schoolCity'),state=formData.get('schoolState'))
            teacher = Teacher.objects.create(firstName=formData.get('firstName'),lastName=formData.get('lastName'),
                              email=formData.get('email'), className=formData.get('className'),school=school)
            school.save()
            teacher.save()
            #create auth user for teacher
            cityUser = CityDigitsUser(role="TEACHER", username=teacher.email,
                                      password=MembershipService.encryptPassword(teacher.email,formData.get('password')),
                                      entityId=teacher.id)
            cityUser.save()

            #create teams and students entities
            teamIdx = 0;
            for teamName in formData.getlist('team_name[]'):
                team = Team.objects.create(name=teamName,teacher=teacher)
                team.save()
                #add students to team
                studentIdx = 0;
                for studentName in formData.getlist("student_name[%s][]"%teamIdx):
                    #get password
                    password = MembershipService.encryptPassword(studentName,formData.getlist("student_password[%s][]"%teamIdx)[studentIdx])
                    #get name
                    student = Student.objects.create(firstName=studentName,team=team)
                    student.save()
                    #create auth user for student
                    print "student password: " + password
                    authUser = CityDigitsUser(role="STUDENT",username=student.firstName,password=password,entityId=student.id)
                    authUser.save()
                    #update index
                    studentIdx = studentIdx + 1

                #updated team index
                teamIdx = teamIdx + 1

            #return response
            json_data = json.dumps({"HTTPRESPONSE":200})
            return HttpResponse(json_data, mimetype="application/json")
        else:
            #form invalid
            #return and display errors
            return render_to_response('signup.html', {'form': form},
                   context_instance=RequestContext(request))
        pass
    elif request.method == 'GET':
        #Load Sign up form
        form = forms.SignUpForm()
        return render_to_response('signup.html', {'form': form},
                   context_instance=RequestContext(request))


def mapNavigation(request):
    """
      Loads the map navigation elements
    """
    return render_to_response('map_navigation.html')


def login(request):
    """
      Handles user login
    """
    if request.method == 'POST':
        #get bound form
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            #attempt to find user username and password
            role = form.cleaned_data["role"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = MembershipService.authenticate(role,username,password)

            #check for authenticated user
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    return HttpResponse(200)
                else:
                    #setup errors to display back to user
                    errors = django.forms.util.ErrorList()
                    errors = form._errors.setdefault(
                    django.forms.forms.NON_FIELD_ERRORS, errors)
                    errors.append('Sorry, this user account is disabled.')
                    return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
            else:
                #setup errors
                errors = django.forms.util.ErrorList()
                errors = form._errors.setdefault(
                django.forms.forms.NON_FIELD_ERRORS, errors)
                errors.append('Username/Password Not Found.')
                return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
        else:
            return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))


    elif request.method == 'GET':
        #Load login form
        form = forms.LoginForm()
        return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))

def logout(request):
    """
     Handles user logout
    """
    print("IN LOGOUT")
    auth_logout(request)
    return HttpResponse(200)


def interview_select(request):
    """
       Interview Select
    """
    return render_to_response('interview_selector.html',context_instance=RequestContext(request))