from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=2, null=False)


    @classmethod
    def create(cls, name, address, city, state):
        school = cls(name=name, address=address, city=city, state=state)
        return school


class Teacher(models.Model):
    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    # password = models.CharField(max_length=128,null=False)
    school = models.ForeignKey(School, null=False)
    className = models.CharField(max_length=255, null=False)


class Team(models.Model):
    name = models.CharField(max_length=6, null=False)
    teacher = models.ForeignKey(Teacher, null=False)


class Student(models.Model):
    firstName = models.CharField(max_length=255, null=False)
    # password = models.CharField(max_length=128,null=False)
    team = models.ForeignKey(Team)


class CityDigitsUserManager(BaseUserManager):
    """
      Custom user manager
    """

    def create_user(self, role, username,
                    password):
        user = self.model(role=role, username=username, password=password)
        return user

    def create_superuser(self, role, username,
                         password):
        user = self.create_user(role, username,
                                password)
        user.is_admin = True
        user.save()
        return user


class CityDigitsUser(AbstractBaseUser):
    role = models.CharField(max_length=7, null=False)
    username = models.CharField(max_length=255, null=False, unique=True)
    # password = models.CharField(max_length=128,null=False)
    entityId = models.IntegerField(null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"

    objects = CityDigitsUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def __unicode__(self):
        return self.username

    def get_short_name(self):
        return self.username


class Location(models.Model):
    """
      Location model
    """
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)


class InterviewPlayer(models.Model):
    """
      Player Interview model
    """
    firstName = models.CharField(max_length=255)
    do_you_ever_buy_lottery_tickets = models.BooleanField()
    why_or_why_not_audio = models.FileField(upload_to="audio/%Y_%m_%d_%h_%M_%s")
    have_you_ever_won_the_lottery = models.BooleanField()
    most_won = models.CharField(max_length=255)
    money_spent_on_lottery_in_average_week = models.CharField(max_length=255)
    jackpot_audio = models.FileField(upload_to="audio/%Y_%m_%d_%h_%M_%s")
    photo = models.FileField(upload_to="photo/%Y_%m_%d_%h_%M_%s")


class InterviewRetailer(models.Model):
    """
      Player Interview model
    """
    storeName = models.CharField(max_length=255)
    do_you_sell_lottery_tickets = models.BooleanField()
    why_or_why_not_audio = models.FileField(upload_to="audio/%Y_%m_%d_%h_%M_%s")
    customers_in_a_day = models.CharField(max_length=255)
    percentage_buy_lottery_tickets = models.IntegerField()
    amount_tickets_bought_per_visit = models.CharField(max_length=50)
    why_or_why_not_lottery_neighborhood_audio = models.FileField(upload_to="audio/%Y_%m_%d_%h_%M_%s")
    photo = models.FileField(upload_to="photo/%Y_%m_%d_%h_%M_%s")
#
# - Do you sell lottery tickets? (yes/no)
# - Why or why not? (add media)
# If 'Do you sell lottery tickets?' = yes:
# - About how many customers do you have in an average day? (integer)
# - What percentage of your customers buy lottery tickets? (integer)
# - About how many tickets do people usually buy in one visit?
# (check boxes: 1 ticket, 2-5 tickets, 6-10 tickets, 11 or more tickets)
# - Do you think the lottery is good for this neighborhood? Why or why not? (add media)
# - Add photo (add media)


class Interview(models.Model):
    """
      Interview model
    """
    student = models.ForeignKey(Student, null=False)
    location = models.ForeignKey(Location, null=False)
    interviewType = models.CharField(max_length=8, null=False)
    entityId = models.IntegerField(null=False)
