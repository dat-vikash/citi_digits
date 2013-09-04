from decimal import Decimal
import json
from random import randint
import django
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.forms.util import ErrorList
from django.forms.formsets import formset_factory
from django.http import HttpResponse, QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
import math
import forms
from models import School, Teacher, Team, Student, CityDigitsUser, Interview, Location, InterviewPlayer, InterviewRetailer, InterviewComment, Tour, TourAuthors, TourSlide, NeighborhoodStatistics
from service import MembershipService
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.utils.html import escape


def index(request):
    """
     Loads base index
    """
     #get random tour
    tourCount = Tour.objects.count()
    tour = Tour.objects.get(pk=(randint(1,tourCount)))

    #get random interview
    interviewCount = Interview.objects.count()
    interview = Interview.objects.get(pk=(randint(1,interviewCount)))
    current_user = request.user
    return render_to_response('index.html', {'tour':tour,'interview':interview},
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

            #check for teacher email unqiueness
            if CityDigitsUser.doesUsernameExist(formData.get('email')):
                #add error and return
                errors = form._errors.setdefault("email", ErrorList())
                errors.append(u"Email already Exists")
                return render_to_response('signup.html', {'form': form},
                                      context_instance=RequestContext(request))

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
            teamIdx = 0
            print(formData)
            for teamName in formData.getlist('team_name[]'):
                teamIdx = teamName.split('_')[1]
                teamName = teamName.split('_')[0]
                team = Team.objects.create(name=teamName, teacher=teacher)
                team.save()
                #add students to team
                studentIdx = 0
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
                # teamIdx = teamIdx + 1

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
    #get all classes
    #get classes
    classes = Teacher.objects.values_list('className', flat=True)
    return render_to_response('map_navigation.html',{'classes':classes},context_instance=RequestContext(request))


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
    #get student team
    team = MembershipService.findStudentForId(request.user.entityId).team.name
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
                                     why_or_why_not_audio=request.FILES['whyOrWhyNot'] if 'whyOrWhyNot' in request.FILES else None,
                                     have_you_ever_won_the_lottery=form.cleaned_data["wonLottery"],
                                     most_won=float(form.cleaned_data["mostWonAmount"] if form.cleaned_data["mostWonAmount"]!="" else 0),
                                     money_spent_on_lottery_in_average_week=float(form.cleaned_data["averageSpentOnLotteryPerWeek"] if form.cleaned_data["averageSpentOnLotteryPerWeek"]!="" else 0 ),
                                     jackpot_audio=request.FILES["wonJackpotQuestion"] if 'wonJackpotQuestion' in request.FILES else None,
                                     photo=request.FILES["photo"] if "photo" in request.FILES else None)
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
            return render_to_response('player_interview.html', {'form': form,'team':team}, context_instance=RequestContext(request))

    elif request.method == "GET":
        #Load interview form
        form = forms.PlayerInterviewForm()
        return render_to_response('player_interview.html', {'form': form,'team':team}, context_instance=RequestContext(request))



@transaction.autocommit
def interviewRetailer(request):
    """
      Handles retailer interview form
    """
    #get student team
    team = MembershipService.findStudentForId(request.user.entityId).team.name
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
                                     why_or_why_not_audio=request.FILES['whyOrWhyNot'] if 'whyOrWhyNot' in request.FILES else None,
                                     customers_in_a_day=form.cleaned_data["customersPerDay"],
                                     percentage_buy_lottery_tickets=float(form.cleaned_data["percentageCustomers"] if form.cleaned_data["percentageCustomers"]!="" else 0),
                                     amount_tickets_bought_per_visit=form.cleaned_data["amountPerVisit"],
                                     why_or_why_not_lottery_neighborhood_audio=request.FILES["goodForNeighborhoodQuestion"] if 'goodForNeighborhoodQuestion' in request.FILES else None,
                                     photo=request.FILES["photo"] if "photo" in request.FILES else None)
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
            return render_to_response('retailer_interview.html', {'form': form,'team':team}, context_instance=RequestContext(request))

    elif request.method == "GET":
        #Load interview form
        form = forms.RetailerInterviewForm()
        return render_to_response('retailer_interview.html', {'form': form,'team':team}, context_instance=RequestContext(request))


def popup(request,layer,neighborhood,perin,dol,sale,win,income,netwin,id):
    """

    """
    if request.method == "GET":
        if layer == "PERCENT_INCOME":
            amountSpent = (100 * (float(perin)/100))
            return render_to_response('map_popup_percent_income.html',{'neighborhood':neighborhood.replace("_"," "),
                'percent':perin, 'amountSpent':amountSpent,'neighborhoodUrl':neighborhood,'income':income},context_instance=RequestContext(request))
        if layer == "MEDIAN_INCOME":
            # neighborhood =  neighborhood.replace("_"," ")
            amountSpent = (100 * (float(perin)/100))
            return render_to_response('map_popup_percent_income.html',{'neighborhood':neighborhood.replace("_"," "),
                'percent':perin, 'amountSpent':amountSpent,'neighborhoodUrl':neighborhood,'income':income},context_instance=RequestContext(request))
        if layer == "NET_GAIN_LOSS":
            # neighborhood =  neighborhood.replace("_"," ")
            return render_to_response('map_popup_net_gain_loss.html',{'id':id,'neighborhood':neighborhood.replace("_"," "),
                'won':win, 'spent':sale},context_instance=RequestContext(request))
        if layer == "AVG_SPEND":
            # neighborhood =  neighborhood.replace("_"," ")
            return render_to_response('map_popup_net_gain_loss.html',{'id':id,'neighborhood':neighborhood.replace("_"," "),
                'won':win, 'spent':sale},context_instance=RequestContext(request))
        if layer == "AVG_WIN":
            # neighborhood =  neighborhood.replace("_"," ")
            return render_to_response('map_popup_net_gain_loss.html',{'id':id,'neighborhood':neighborhood.replace("_"," "),
                'won':win, 'spent':sale},context_instance=RequestContext(request))

def mathExplain(request,neighborhood,spent,income):
    """

    """
    neighborhood =  neighborhood.replace("_"," ")
    spent = float(spent)
    modCount = divmod(float(income),100)[0]
    modCount = range(0,int(modCount))
    leftOver = float(divmod(float(income),100)[1]) / float(100) * float(spent)
    spentOnLotto = float(spent) * float(income) / float(100)
    yearSpent = spentOnLotto * 365
    yearEarned = Decimal(income) * 365
    return render_to_response('mathematical_explainations.html',{'neighborhood':neighborhood, 'spent':spent,
                                                                 'income':income,'modCount':modCount, 'yearEarned':yearEarned,
                                                                 'leftOver':leftOver,'yearSpent':yearSpent,
                                                                 'spentOnLotto':spentOnLotto},context_instance=RequestContext(request))


def notAllEqual(request,neighborhood):
    """
     Not all equal explaination
    """
    #get stats based on neighborhood
    stats = NeighborhoodStatistics.objects.get(pk=neighborhood)
    totalAdults = stats.total_18_and_up
    totalStores = stats.total_retailers
    neighborhood =  stats.name
    adultsPerStore = stats.adults_per_store
    netLossList = range(0,int(abs(round(float(stats.net_loss_per_store)/100.0))))
    netLoss =abs(float(stats.net_loss_per_store))
    personList = range(0,int(round(float(stats.adults_per_store)/100.0)))
    statsHuntersPoint = NeighborhoodStatistics.objects.get(pk=241)
    netLossListHP = range(0,int(abs(round(float(statsHuntersPoint.net_loss_per_store)/100.0))))
    personListHP = range(0,int(round(float(statsHuntersPoint.adults_per_store)/100.0)))
    statsHillCrest = NeighborhoodStatistics.objects.get(pk=210)
    netLossListHILL = range(0,int(abs(round(float(statsHillCrest.net_loss_per_store)/100.0))))
    personListHILL = range(0,int(round(float(statsHillCrest.adults_per_store)/100.0)))
    adultsPerStoreHILL = statsHillCrest.adults_per_store
    adultsPerStoreHP = statsHuntersPoint.adults_per_store
    netLossHILL = abs(float(statsHillCrest.net_loss_per_store))
    netLossHP = abs(float(statsHuntersPoint.net_loss_per_store))

    return render_to_response('not_all_equal.html',{'neighborhood':neighborhood, 'totalAdults':totalAdults,
                                                    'totalStores':totalStores,'adultsPerStore':adultsPerStore,
                                                    'netLossList':netLossList,'netLoss':netLoss,
                                                    'personList': personList,'personListHP':personListHP,'netLossListHP':netLossListHP,
                                                    'netLossListHILL':netLossListHILL,'personListHILL':personListHILL,
                                                    'adultsPerStoreHILL':adultsPerStoreHILL,'adultsPerStoreHP':adultsPerStoreHP,
                                                    'netLossHILL':netLossHILL,'netLossHP':netLossHP
                                                    },context_instance=RequestContext(request))


def loadGeoJsonInterviews(request):
    """

    """
    #get all interviews
    type = request.GET.get("type",None)
    allInterview = None

    if(type):
        if(type in ('PLAYER','RETAILER')):
            allInterview = Interview.objects.filter(interviewType=type)
        else:
            allInterview = Interview.objects.filter(student__team__teacher__className__exact=type)
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
                                        "interview_id": interview.id,
                                        "photo": str(interview.getInterview().photo),
                                        "name": interview.getInterview().firstName if interview.interviewType == "PLAYER" else interview.getInterview().storeName,
                                        "team": interview.student.team.name,
                                        "class": interview.student.team.teacher.className
                                    }})

    return HttpResponse(json.dumps(geoJson), content_type="application/json")


def interviewList(request,offset):
    """
        This view returns the interviews based on search criteria
    """
    offset = int(offset)
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

     #get paginated tours
    interviews = __paginatatedEntities(interviews,offset)

    #calculate pages to display
    pagesToDisplay = range(1,interviews.paginator.num_pages)

    if(offset == 1):
        pagesToDisplay = pagesToDisplay[0:offset+5]
    else:
        idxStart= offset - 2
        if (idxStart > 0):
            pagesToDisplay = pagesToDisplay[idxStart:idxStart+5]
        else:
            pagesToDisplay = pagesToDisplay[0:offset+5]


    #render
    print toolbar
    return render_to_response('interviews.html',{'interviews':interviews,'teams':teams, 'classes':classes,
                                                 'toolbar':toolbar,'pages_to_display':pagesToDisplay},context_instance=RequestContext(request))

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
    current_user = request.user
    #get class
    currentStudent = Student.objects.get(pk=current_user.entityId)
    studentClass = currentStudent.team.teacher.className
    students = Student.objects.filter(team__teacher__className=studentClass)

    SlideFormSet = formset_factory(forms.TourSlide,extra=1)
    if request.method == 'POST':
        #create forms
        tourForm = forms.TourForm(request.POST,request.FILES)
        slideFormset = SlideFormSet(request.POST,request.FILES)

        #validate forms
        if tourForm.is_valid() and slideFormset.is_valid():
            #create tour
            newTour = Tour(title=tourForm.cleaned_data['title'],teamPhoto=tourForm.cleaned_data["teamPhoto"],student=currentStudent)
            newTour.save()

            #create tour authors
            for authorId in request.POST.getlist('authors[]',[]):
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
                if(slide.cleaned_data['isCoverPhoto']):
                    #set cover photo
                    newTour.coverPhoto = slide.cleaned_data['image']
                    newTour.save()
                slideIdx= slideIdx + 1


             #return response
            json_data = json.dumps({"HTTPRESPONSE": 200})
            return HttpResponse(json_data, mimetype="application/json")
        else:
            return render_to_response('add_a_tour.html',{'tour':tourForm,'slide_formset':slideFormset,'students':students},context_instance=RequestContext(request))

    else:
        #get request
        #tour form
        tour = forms.TourForm()
        #tour slides
        slide_formset = SlideFormSet()
        #students
        return render_to_response('add_a_tour.html',{'tour':tour,'slide_formset':slide_formset,'students':students},context_instance=RequestContext(request))


def tourPreview(request):
    """
      Previews a tour
    """
    slideCount = request.GET.get("slides",0)
    slideCount = range(0,int(slideCount))
    return render_to_response('tour_preview.html',{'slides':slideCount},context_instance=RequestContext(request))

def tourList(request,offset):
    """
     Handles displaying tour grid
    """
    #store toolbar form info
    offset = int(offset)
    toolbar={'searchClass':'ALL',
             'sortDate':'DESC'}

    #get search teams
    sortDate = request.GET.get("sort-date","DESC")
    print "date: " + sortDate
    if sortDate == "":sortDate = "DESC"
    print "date: " + sortDate

    #get search class
    searchClass = request.GET.get("sort-class","ALL")
    if searchClass == "":searchClass = "ALL"

    #build query
    kwargs = {}
    if(searchClass != "ALL"):
        kwargs['student__team__teacher__className__exact'] = searchClass
        toolbar['searchClass'] = searchClass


    #get tours
    tours = None
    if(sortDate == "DESC"):
        tours = Tour.objects.filter(**kwargs).order_by('-created_at')
        toolbar['sortDate'] = "DESC"
    if(sortDate == "ASC"):
        tours = Tour.objects.filter(**kwargs).order_by('created_at')
        toolbar['sortDate'] = "ASC"


    #get classes
    classes = Teacher.objects.values_list('className', flat=True)

    #get paginated tours
    tours = __paginatatedEntities(tours,offset)

    #calculate pages to display
    pagesToDisplay = range(1,tours.paginator.num_pages)
    print pagesToDisplay

    if(offset == 1):
        pagesToDisplay = pagesToDisplay[0:offset+5]
    else:
        idxStart= offset - 2
        if (idxStart > 0):
            pagesToDisplay = pagesToDisplay[idxStart:idxStart+5]
        else:
            pagesToDisplay = pagesToDisplay[0:offset+5]



    #render
    print toolbar
    return render_to_response('tours.html',{'tours':tours, 'classes':classes,'toolbar':toolbar,'pages_to_display':pagesToDisplay}
        ,context_instance=RequestContext(request))


def tourDetails(request,id):
    """
    Loads tour details
    """
    tour = Tour.objects.get(pk=id)
    return render_to_response('tour_details.html',{'tour':tour},context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',{},context_instance=RequestContext(request))

def home(request):
    """
      Home page
    """
    print "in home page"
    #get random tour
    tourCount = Tour.objects.count()
    tour = Tour.objects.get(pk=(randint(1,tourCount)))

    #get random interview
    interviewCount = Interview.objects.count()
    interview = Interview.objects.get(pk=(randint(1,interviewCount)))

    return render_to_response('home.html',{'tour':tour,'interview':interview}, context_instance=RequestContext(request))




###############################
##  View Helper Methods      ##
###############################

def __paginatatedEntities(entity,page):
    """
       Returns a list of paginated entities
    """
    entities = None
    #pages per page
    paginator = Paginator(entity,9)

    #pagination
    try:
        entities = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        entities = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        entities = paginator.page(paginator.num_pages)
    finally:
        return entities


