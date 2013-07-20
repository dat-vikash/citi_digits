from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255,null=False)
    address = models.CharField(max_length=255,null=False)
    city = models.CharField(max_length=255,null=False)
    state = models.CharField(max_length=2,null=False)


    @classmethod
    def create(cls, name,address,city,state):
        school = cls(name=name,address=address,city=city,state=state)
        return school

class Teacher(models.Model):
    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255,null=False)
    password = models.CharField(max_length=128,null=False)
    school = models.ForeignKey(School,null=False)
    className = models.CharField(max_length=255,null=False)

class Team(models.Model):
    name = models.CharField(max_length=6,null=False)
    teacher = models.ForeignKey(Teacher,null=False)

class Student(models.Model):
    firstName = models.CharField(max_length=255,null=False)
    password = models.CharField(max_length=128,null=False)
    team = models.ForeignKey(Team)



