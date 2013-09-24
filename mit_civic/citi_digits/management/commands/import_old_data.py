import os
from django.core.management.base import BaseCommand, CommandError
from citi_digits.models import School, Teacher, CityDigitsUser, Team, Student, InterviewPlayer, Interview, Location, InterviewRetailer
from citi_digits.service import MembershipService
import csv
import urllib2
from dateutil.parser import parse
from django.conf import settings as SETTINGS

__author__ = 'vikash'

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def create_school(self):
        """

        """
        school = School.objects.create(name="Bushwick School for Social Justice", address="400 Irving Ave",
                                               city="New York", state="NY")
        school.save()
        return school

    def create_teacher(self,school):
        """

        """
        teacher = Teacher.objects.create(firstName="Lauren", lastName="Shookhoff",
                                                 email="edeahl@mit.edu", className="Ms. Shookhoff's Class",
                                                 school=school)
        teacher.save()
        return teacher


    def create_auth_account(self,teacher):
        """
        """
        cityUser = CityDigitsUser(role="TEACHER", username=teacher.email,
                                          password=MembershipService.encryptPassword(teacher.email,
                                                                                     "citydigits"),
                                          entityId=teacher.id, is_active=True)
        cityUser.save()

    def create_teams(self,teacher):
        """

        """
        team_pink = Team.objects.create(name="PINK", teacher=teacher)
        team_pink.save()

        team_red = Team.objects.create(name="RED", teacher=teacher)
        team_red.save()

        team_blue = Team.objects.create(name="BLUE", teacher=teacher)
        team_blue.save()

        team_green = Team.objects.create(name="GREEN", teacher=teacher)
        team_green.save()

        return (team_pink,team_red,team_blue,team_green)

    def create_students(self,teams):
        """

        """

        #get password
        password = MembershipService.encryptPassword("student_pink",
                                                     "citydigits")
        #get name
        student1 = Student.objects.create(firstName="student_pink", team=teams[0])
        student1.save()
        #create auth user for student
        authUser1 = CityDigitsUser(role="STUDENT", username=student1.firstName, password=password,
                                  entityId=student1.id,is_active=True)
        authUser1.save()


        #get password
        password = MembershipService.encryptPassword("student_red",
                                                     "citydigits")
        #get name
        student2 = Student.objects.create(firstName="student_red", team=teams[1])
        student2.save()
        #create auth user for student
        authUser2 = CityDigitsUser(role="STUDENT", username=student2.firstName, password=password,
                                  entityId=student2.id, is_active=True)
        authUser2.save()


        #get password
        password = MembershipService.encryptPassword("student_blue",
                                                     "citydigits")
        #get name
        student3 = Student.objects.create(firstName="student_blue", team=teams[2])
        student3.save()
        #create auth user for student
        authUser3= CityDigitsUser(role="STUDENT", username=student3.firstName, password=password,
                                  entityId=student3.id, is_active=True)
        authUser3.save()


        #get password
        password = MembershipService.encryptPassword("student_green",
                                                     "citydigits")
        #get name
        student4 = Student.objects.create(firstName="student_green", team=teams[3])
        student4.save()
        #create auth user for student
        authUser4 = CityDigitsUser(role="STUDENT", username=student4.firstName, password=password,
                                  entityId=student4.id, is_active=True)
        authUser4.save()


        return (student1,student2,student3,student4)

    def create_player_interview(self,row,students):
        """
        """
        name = row[3]
        do_you_buy = 0
        #do you buy lottery tickets
        if(row[4]=="Yes"):
            do_you_buy = 1
        if(row[4]=="No"):
            do_you_buy = 0

        #why or why not audio
        #download audio to directory
        why_why_not_path = ""
        if(row[5]!=""):
            try:
                request_end = row[5].find('"',33)
                url = row[5][33:request_end]
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)

                #grab the data
                data = response.read()
                filename = url.split('/')[len(url.split('/'))-1]
                why_why_not_path = "backup/" + filename;
                why_why_not = open(SETTINGS.MEDIA_ROOT + "/backup/" + filename, "wb")
                why_why_not.write(data)    # was data2
                why_why_not.close()
            except Exception as e:
                print e
                print url

        #ever won lottery
        ever_won = 0
        if(row[6]=="Yes"):
            ever_won = 1

        most_won = row[7]

        money_per_week = row[8]

        #jackpot audio
        jackpot_audio_path = ""
        if(row[9]!=""):
            try:
                request_end = row[9].find('"',59)
                url = row[9][59:request_end]
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)

                #grab the data
                data = response.read()
                filename = url.split('/')[len(url.split('/'))-1]
                jackpot_audio_path = "backup/" + filename;
                jackpot_audio = open(SETTINGS.MEDIA_ROOT + "/backup/" + filename, "wb")
                jackpot_audio.write(data)    # was data2
                jackpot_audio.close()
            except Exception as e:
                print "JACKOUT EXCPETION: " + e.message

        #photo
        photo_path = ""
        if(row[10]!=""):
            url = row[10]
            try:
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)

                #grab the data
                data = response.read()
                filename = url.split('/')[len(url.split('/'))-1]
                photo_path = "backup/" + filename;
                photo = open(SETTINGS.MEDIA_ROOT + "/backup/" + filename, "wb")
                photo.write(data)    # was data2
                photo.close()
            except Exception as e:
                print e
                print url

        #create interview
        entity = InterviewPlayer(firstName=name,
                                 do_you_ever_buy_lottery_tickets=do_you_buy,
                                 why_or_why_not_audio=why_why_not_path,
                                 have_you_ever_won_the_lottery=ever_won,
                                 most_won=float(most_won if most_won!="" else 0),
                                 money_spent_on_lottery_in_average_week=float(money_per_week if money_per_week!="" else 0),
                                 jackpot_audio=jackpot_audio_path,
                                 photo=photo_path)
        entity.save()

        return entity.id

    def create_retailer_interview(self,row,students):
        """
        """
        name = row[3]
        do_you_sell = 1

        #why or why not audio
        #download audio to directory
        why_why_not_path = ""


        #customers in a day
        customers_in_a_day = row[4]

        #percentage buy lotto
        percentage_buy_lotto = row[5]

        #amount of tickets bought per visit
        amount_tickets_per_visit = row[6]
        if(amount_tickets_per_visit=="1 ticket"):
            amount_tickets_per_visit="1-TICKET"
        if(amount_tickets_per_visit=="2-5 tickets"):
            amount_tickets_per_visit="2-5-TICKETS"
        if(amount_tickets_per_visit=="6-10 tickets"):
            amount_tickets_per_visit="6-10-TICKETS"
        if(amount_tickets_per_visit=="11 or more tickets"):
            amount_tickets_per_visit="11-OR-MORE-TICKETS"
        if(amount_tickets_per_visit=="2-5 tickets; 11 or more tickets"):
            amount_tickets_per_visit="11-OR-MORE-TICKETS"

        #ahy or why not 2 audio
        good_for_neighborhood_path = ""
        if(row[7]!="" and row[7]!="[no response recorded]"):
            try:
                request_end = row[7].find('"',89)
                url = row[7][89:request_end]
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)

                #grab the data
                data = response.read()
                filename = url.split('/')[len(url.split('/'))-1]
                good_for_neighborhood_path = "backup/" + filename;
                jackpot_audio = open(SETTINGS.MEDIA_ROOT + "/backup/" + filename, "wb")
                jackpot_audio.write(data)    # was data2
                jackpot_audio.close()
            except Exception as e:
                print "GOOD FOR NEIGHBORHOOD EXCPETION: " + e.message

        #photo
        photo_path = ""
        if(row[8]!=""):
            url = row[8]
            try:
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)

                #grab the data
                data = response.read()
                filename = url.split('/')[len(url.split('/'))-1]
                photo_path = "backup/" + filename;
                photo = open(SETTINGS.MEDIA_ROOT + "/backup/" + filename, "wb")
                photo.write(data)    # was data2
                photo.close()
            except Exception as e:
                print e
                print url

        #create interview
        entity = InterviewRetailer(storeName=name,
                                     do_you_sell_lottery_tickets=do_you_sell,
                                     why_or_why_not_audio=why_why_not_path,
                                     customers_in_a_day=customers_in_a_day,
                                     percentage_buy_lottery_tickets=float(percentage_buy_lotto if percentage_buy_lotto!="" else 0),
                                     amount_tickets_bought_per_visit=amount_tickets_per_visit,
                                     why_or_why_not_lottery_neighborhood_audio=good_for_neighborhood_path,
                                     photo=photo_path)
        entity.save()

        return entity.id



    def create_interview(self,id, row,students, type):
        """
        """
        stud = None
        lat = None
        long = None
        address = None
        #determine student
        if(type=="PLAYER"):
            if(row[14]=="Pink"):
                stud = students[0]
            if(row[14]=="Red"):
                stud = students[1]
            if(row[14]=="Blue"):
                stud = students[2]
            if(row[14]=="Green"):
                stud = students[3]
            lat = row[12]
            long = row[13]
            address = row[11]
        if(type=="RETAILER"):
            if(row[12]=="Pink"):
                stud = students[0]
            if(row[12]=="Red"):
                stud = students[1]
            if(row[12]=="Blue"):
                stud = students[2]
            if(row[12]=="Green"):
                stud = students[3]
            lat = row[10]
            long = row[11]
            address = row[9]

        #create location
        location = Location(latitude=lat, longitude=long,
                                    address=address)
        location.save()


        #Create interview
        interview = Interview(student=stud, location=location, interviewType=type, entityId=id,created_at=parse(row[0]).strftime("%Y-%m-%d %H:%M:%S"))
        interview.save()

    def create_interviews(self,students):
        """

        """
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        #open player csv export
        with open(os.path.join(__location__, 'exported_data.csv'), 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                #create player interview
                id = self.create_player_interview(row,students)
                #create interview
                self.create_interview(id,row,students,"PLAYER")

        #open retailer csv export
        with open(os.path.join(__location__, 'exported_data_retailer.csv'), 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                #create player interview
                id = self.create_retailer_interview(row,students)
                #create interview
                self.create_interview(id,row,students,"RETAILER")

    def handle(self, *args, **options):
        print "CREATING SCHOOL......"
        school = self.create_school()
        print "CREATING TEACHER....."
        teacher = self.create_teacher(school)
        print "CREATING AUTH FOR TEACHER...."
        self.create_auth_account(teacher)
        print "CREATING TEAMS....."
        teams = self.create_teams(teacher)
        print "CREATING STUDENTS...."
        students = self.create_students(teams)
        print "CREATING INTERVIEWS...."
        self.create_interviews(students)





