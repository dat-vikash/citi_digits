import json
from django.db import transaction
from django.http import HttpResponse, QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
import forms
from models import School, Teacher, Team, Student
from service import MembershipService


def index(request):
    """
     Loads base index
    """
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
            #set password
            teacher.password = MembershipService.encryptPassword(teacher.lastName,formData.get('password'))
            school.save()
            teacher.save()

            #create teams and students entities
            teamIdx = 0;
            for teamName in formData.getlist('team_name[]'):
                team = Team.objects.create(name=teamName,teacher=teacher)
                team.save()
                #add students to team
                studentIdx = 0;
                for studentName in formData.getlist("student_name[%s][]"%teamIdx):
                    #get password
                    password = MembershipService.encryptPassword(studentName,formData.getlist("student_name[%s][]"%teamIdx)[studentIdx])
                    #get name
                    student = Student.objects.create(firstName=studentName,team=team,password=password)
                    student.save()
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