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


class Interview(models.Model):
    """
      Interview model
    """
    student = models.ForeignKey(Student, null=False)
    location = models.ForeignKey(Location, null=False)
    interviewType = models.CharField(max_length=8, null=False)
    entityId = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add = True,null=False)

    def getInterview(self):
        """

        """
        if self.interviewType == "RETAILER":
            return InterviewRetailer.objects.get(pk=self.entityId)
        if self.interviewType == "PLAYER":
            return InterviewPlayer.objects.get(pk=self.entityId)

class InterviewComment(models.Model):
    """
     Interview Comment
    """
    name = models.CharField(max_length=255,null=False)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    interview = models.ForeignKey(Interview)


class Tour(models.Model):
    """
     Tour
    """
    title = models.CharField(max_length=255,null=False)
    teamPhoto = models.FileField(upload_to="photo/%Y_%m_%d_%h_%M_%s_team_photo")
    coverPhoto = models.FileField(upload_to="photo/%Y_%m_%d_%h_%M_%s_cover_photo")
    created_at = models.DateTimeField(auto_now_add = True,null=False)
    student = models.ForeignKey(Student)

class TourAuthors(models.Model):
    """
    Tour Authors
    """
    student = models.ForeignKey(Student)
    tour = models.ForeignKey(Tour)


class TourSlide(models.Model):
    """
     Tour Slides
    """
    photo = models.FileField(upload_to="photo/%Y_%m_%d_%h_%M_%s_slide_photo")
    text = models.TextField(null=False)
    link = models.TextField(null=False)
    audio = models.FileField(upload_to="audio/%Y_%m_%d_%h_%M_%s_slide_audio")
    tour = models.ForeignKey(Tour)
    sequence = models.IntegerField(null=False)