import json
import django
from django.db import transaction
from django.forms.formsets import formset_factory
from django.http import HttpResponse, QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
import forms
from models import School, Teacher, Team, Student, CityDigitsUser, Interview, Location, InterviewPlayer, InterviewRetailer, InterviewComment, Tour, TourAuthors, TourSlide
from service import MembershipService
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.utils.html import escape


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
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            #place form data into query dict for easier access
            formData = QueryDict(request.body)
            #create entities
            school = School.objects.create(name=formData.get('schoolName'), address=formData.get('schoolAddress'),
                                           city=formData.get('schoolCity'), state=formData.get('schoolState'))
            teacher = Teacher.objects.create(firstName=formData.get('firstName'), lastName=formData.get('lastName'),
                                             email=formData.get('email'), className=formData.get('className'),
                                             school=school)
            school.save()
            teacher.save()
            #create auth user for teacher
            cityUser = CityDigitsUser(role="TEACHER", username=teacher.email,
                                      password=MembershipService.encryptPassword(teacher.email,
                                                                                 formData.get('password')),
                                      entityId=teacher.id)
            cityUser.save()

            #create teams and students entities
            teamIdx = 0;
            for teamName in formData.getlist('team_name[]'):
                team = Team.objects.create(name=teamName, teacher=teacher)
                team.save()
                #add students to team
                studentIdx = 0;
                for studentName in formData.getlist("student_name[%s][]" % teamIdx):
                    #get password
                    password = MembershipService.encryptPassword(studentName,
                                                                 formData.getlist("student_password[%s][]" % teamIdx)[
                                                                     studentIdx])
                    #get name
                    student = Student.objects.create(firstName=studentName, team=team)
                    student.save()
                    #create auth user for student
                    print "student password: " + password
                    authUser = CityDigitsUser(role="STUDENT", username=student.firstName, password=password,
                                              entityId=student.id)
                    authUser.save()
                    #update index
                    studentIdx = studentIdx + 1

                #updated team index
                teamIdx = teamIdx + 1

            #return response
            json_data = json.dumps({"HTTPRESPONSE": 200})
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
            user = MembershipService.authenticate(role, username, password)

            #check for authenticated user
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponse(200)
                else:
                    #setup errors to display back to user
                    errors = django.forms.util.ErrorList()
                    errors = form._errors.setdefault(
                        django.forms.forms.NON_FIELD_ERRORS, errors)
                    errors.append('Sorry, this user account is disabled.')
                    return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
            else:
                #setup errors
                errors = django.forms.util.ErrorList()
                errors = form._errors.setdefault(
                    django.forms.forms.NON_FIELD_ERRORS, errors)
                errors.append('Username/Password Not Found.')
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


    elif request.method == 'GET':
        #Load login form
        form = forms.LoginForm()
        return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


def logout(request):
    """
     Handles user logout
    """
    auth_logout(request)
    return HttpResponse(200)


def interviewSelect(request):
    """
       Interview Select
    """
    return render_to_response('interview_selector.html', context_instance=RequestContext(request))


@transaction.autocommit
def interviewPlayer(request):
    """
      Handles player interview form
    """
    if request.method == "POST":
        #Bound form
        form = forms.PlayerInterviewForm(request.POST, request.FILES)
        if form.is_valid():
            #Save interview related information
            #Get student
            student = MembershipService.findStudentForId(request.user.entityId)
            #Create location
            location = Location(latitude=form.cleaned_data['latitude'], longitude=form.cleaned_data["longitude"],
                                address=form.cleaned_data["location"])
            location.save()
            #Create player profile
            entity = None
            entity = InterviewPlayer(firstName=form.cleaned_data["firstName"],
                                     do_you_ever_buy_lottery_tickets=form.cleaned_data["buyLotteryTickets"],
                                     why_or_why_not_audio=request.FILES['whyOrWhyNot'],
                                     have_you_ever_won_the_lottery=form.cleaned_data["wonLottery"],
                                     most_won=float(form.cleaned_data["mostWonAmount"]),
                                     money_spent_on_lottery_in_average_week=float(form.cleaned_data["averageSpentOnLotteryPerWeek"]),
                                     jackpot_audio=request.FILES["wonJackpotQuestion"],
                                     photo=request.FILES["photo"])
            entity.save()
            #Create interview
            interview = Interview(student=student, location=location, interviewType="PLAYER", entityId=entity.id)
            interview.save()
            #return response
            json_data = json.dumps({"HTTPRESPONSE": 200})
            return HttpResponse(json_data, mimetype="application/json")
        else:
            print("FORM ERRORS")
            for e in form.errors:
                print e
            return render_to_response('player_interview.html', {'form': form}, context_instance=RequestContext(request))

    elif request.method == "GET":
        #Load interview form
        form = forms.PlayerInterviewForm()
        #get student team
        team = MembershipService.findStudentForId(request.user.entityId).team.name
        return render_to_response('player_interview.html', {'form': form,'team':team}, context_instance=RequestContext(request))



@transaction.autocommit
def interviewRetailer(request):
    """
      Handles retailer interview form
    """
    if request.method == "POST":
        #Bound form
        form = forms.RetailerInterviewForm(request.POST, request.FILES)
        if form.is_valid():
            #Save interview related information
            #Get student
            student = MembershipService.findStudentForId(request.user.entityId)
            #Create location
            location = Location(latitude=form.cleaned_data['latitude'], longitude=form.cleaned_data["longitude"],
                                address=form.cleaned_data["location"])
            location.save()
            #Create retailer profile
            entity = None
            entity = InterviewRetailer(storeName=form.cleaned_data["storeName"],
                                     do_you_sell_lottery_tickets=form.cleaned_data["sellLotteryTickets"],
                                     why_or_why_not_audio=request.FILES['whyOrWhyNot'],
                                     customers_in_a_day=form.cleaned_data["customersPerDay"],
                                     percentage_buy_lottery_tickets=float(form.cleaned_data["percentageCustomers"]),
                                     amount_tickets_bought_per_visit=form.cleaned_data["amountPerVisit"],
                                     why_or_why_not_lottery_neighborhood_audio=request.FILES["goodForNeighborhoodQuestion"],
                                     photo=request.FILES["photo"])
            entity.save()
            #Create interview
            interview = Interview(student=student, location=location, interviewType="RETAILER", entityId=entity.id)
            interview.save()
            #return response
            json_data = json.dumps({"HTTPRESPONSE": 200})
            return HttpResponse(json_data, mimetype="application/json")
        else:
            print("FORM ERRORS")
            for e in form.errors:
                print e
            return render_to_response('retailer_interview.html', {'form': form}, context_instance=RequestContext(request))

    elif request.method == "GET":
        #Load interview form
        form = forms.RetailerInterviewForm()
        #get student team
        team = MembershipService.findStudentForId(request.user.entityId).team.name
        return render_to_response('retailer_interview.html', {'form': form,'team':team}, context_instance=RequestContext(request))


def popup(request,layer,neighborhood,perin,dol,sale,win,income,netwin):
    """

    """
    if request.method == "GET":
        if layer == "PERCENT_INCOME":
            amountSpent = (100 * (float(perin)/100))
            return render_to_response('map_popup_percent_income.html',{'neighborhood':neighborhood.replace("_"," "),
                'percent':perin, 'amountSpent':amountSpent,'neighborhoodUrl':neighborhood,'income':income},context_instance=RequestContext(request))
        if layer == "MEDIAN_INCOME":
            neighborhood =  neighborhood.replace("_"," ")
            amountSpent = (100 * (float(perin)/100))
            return render_to_response('map_popup_percent_income.html',{'neighborhood':neighborhood.replace("_"," "),
                'percent':perin, 'amountSpent':amountSpent,'neighborhoodUrl':neighborhood,'income':income},context_instance=RequestContext(request))
        if layer == "NET_GAIN_LOSS":
            neighborhood =  neighborhood.replace("_"," ")
            return render_to_response('map_popup_net_gain_loss.html',{'neighborhood':neighborhood.replace("_"," "),
                'won':win, 'spent':sale},context_instance=RequestContext(request))
        if layer == "AVG_SPEND":
            neighborhood =  neighborhood.replace("_"," ")
            return render_to_response('map_popup_net_gain_loss.html',{'neighborhood':neighborhood.replace("_"," "),
                'won':win, 'spent':sale},context_instance=RequestContext(request))
        if layer == "AVG_WIN":
            neighborhood =  neighborhood.replace("_"," ")
            return render_to_response('map_popup_net_gain_loss.html',{'neighborhood':neighborhood.replace("_"," "),
                'won':win, 'spent':sale},context_instance=RequestContext(request))

def mathExplain(request,neighborhood,spent,income):
    """

    """
    neighborhood =  neighborhood.replace("_"," ")
    return render_to_response('mathematical_explainations.html',{'neighborhood':neighborhood, 'spent':spent, 'income':income},context_instance=RequestContext(request))



def loadGeoJsonInterviews(request):
    """

    """
    #get all interviews
    type = request.GET.get("type",None)
    allInterview = None

    if(type):
        allInterview = Interview.objects.filter(interviewType=type)
    else:
        allInterview = Interview.objects.all()


    geoJson = {"type":"FeatureCollection",
               "features":[]}

    #create features
    for interview in allInterview:
        markerType = interview.interviewType.lower()
        geoJson["features"].append({"type":"Feature","geometry":{"type":"Point","coordinates":[interview.location.longitude,interview.location.latitude]},
                                    "properties":{
                                        "icon": {
                                            "iconUrl": "/static/img/" + markerType + "marker_" + interview.student.team.name.lower() +".png",
                                            "iconSize": [50, 50],
                                            "iconAnchor": [25, 25],
                                            "popupAnchor": [0, -25] },
                                        "interview_id": interview.id
                                    }})

    return HttpResponse(json.dumps(geoJson), content_type="application/json")


def interviewList(request,offset):
    """
        This view returns the interviews based on search criteria
    """
    #store toolbar form info
    toolbar={'player':True,
             'retailer':True,
             'searchClass':'ALL',
             'searchTeam':'ALL'}

    #get interview types
    playerType = request.GET.get("player","false")
    retailerType = request.GET.get("retailer","false")

    #get search teams
    searchTeam = request.GET.get("team","ALL")

    #get search class
    searchClass = request.GET.get("class","ALL")
    #build query
    kwargs = {}
    if(playerType == "true" and retailerType == "false"):
        kwargs['interviewType__exact'] = "PLAYER"
        toolbar['retailer'] = False

    if(playerType =="false" and retailerType=="true"):
        kwargs['interviewType__exact'] = "RETAILER"
        toolbar['player'] = False

    if(searchClass != "ALL"):
        kwargs['student__team__teacher__className__exact'] = searchClass
        toolbar['searchClass'] = searchClass

    if(searchTeam != "ALL"):
        kwargs['student__team__name__exact'] = searchTeam
        toolbar['searchTeam'] = searchTeam


    #get interviews
    print kwargs
    interviews = Interview.objects.filter(**kwargs)

    #get teams
    teams =  Team.objects.values_list('name', flat=True).order_by('name').distinct()

    #get classes
    classes = Teacher.objects.values_list('className', flat=True)

    #render
    print toolbar
    return render_to_response('interviews.html',{'interviews':interviews,'teams':teams, 'classes':classes,'toolbar':toolbar},context_instance=RequestContext(request))

def interviewDetails(request,id):
    """
        Interview details
    """
    #get interview from id
    interview = Interview.objects.get(pk=id)
    comments = InterviewComment.objects.filter(interview=interview)
    (long,lat)=(interview.location.longitude,interview.location.latitude)
    return render_to_response('interview_details.html',{'interview':interview,'long':long,'lat':lat,
                                                        'comments':comments},context_instance=RequestContext(request))


@transaction.autocommit
def comment(request,id):
    """
      Posts a comment to an interview
    """
    if request.method == 'POST':
        #get variables
        print request.POST
        name = request.POST.get('name',None)
        message = escape(request.POST.get('comment',''))
        print "NAME: " + name

        if name is not None:
            #get interview
            interview = Interview.objects.get(pk=id)
            #create comment
            comment = InterviewComment(name=name,comment=message,interview=interview)
            #persist comment
            comment.save()
            #get comments
            comments = InterviewComment.objects.filter(interview=interview)
            return render_to_response('interview_details_comments.html',{'comments':comments},context_instance=RequestContext(request))
        else:
            print "name is none"
            return HttpResponse(json.dumps({"HTTPRESPONSE": 500}), content_type="application/json")



@transaction.autocommit
def tour(request):
    """
     Handles adding a tour
    """
    SlideFormSet = formset_factory(forms.TourSlide,extra=1)
    if request.method == 'POST':
        #create forms
        tourForm = forms.TourForm(request.POST,request.FILES)
        slideFormset = SlideFormSet(request.POST,request.FILES)

        #validate forms
        if tourForm.is_valid() and slideFormset.is_valid():
            #create tour
            newTour = Tour(title=tourForm.cleaned_data['title'],teamPhoto=tourForm.cleaned_data["teamPhoto"])
            newTour.save()

            #create tour authors
            for authorId in request.POST.getlist('authors[]',[]):
                print "getting authors"
                #get student
                student = Student.objects.get(pk=authorId)
                #create tour author
                author = TourAuthors(student=student,tour=newTour)
                author.save()

            #create tour slides
            slideIdx=1
            for slide in slideFormset.forms:
                TourSlide(photo=slide.cleaned_data['image'],text=slide.cleaned_data['text'],
                          link=slide.cleaned_data['link'],tour=newTour,sequence=slideIdx,audio=slide.cleaned_data['audio']).save()
                slideIdx= slideIdx + 1


        else:
            #form is invalid, return errors
            students = Student.objects.all()
            return render_to_response('add_a_tour.html',{'tour':tourForm,'slide_formset':slideFormset,'students':students},context_instance=RequestContext(request))

    else:
        #get request
        #tour form
        tour = forms.TourForm()
        #tour slides
        slide_formset = SlideFormSet()
        #students
        students = Student.objects.all()
        return render_to_response('add_a_tour.html',{'tour':tour,'slide_formset':slide_formset,'students':students},context_instance=RequestContext(request))


def tourPreview(request):
    """
      Previews a tour
    """
    slideCount = request.GET.get("slides",0)
    slideCount = range(0,int(slideCount))
    return render_to_response('tour_preview.html',{'slides':slideCount},context_instance=RequestContext(request))