"""
This file contains both unit tests and functional tests for the citi digits application. These will run
when you run "manage.py test".

"""
from django.db import IntegrityError

from django.test import LiveServerTestCase
from unittest import TestCase
from selenium import webdriver
from django.test import Client
from models import *
from service import MembershipService

# Model Unit Tests

class StudentUnitTest(TestCase):

    def setUp(self):
        self.FIRST_NAME = "TEST FIRST NAME"
        self.PASSWORD = MembershipService.encryptPassword(self.FIRST_NAME,"PASSWORD")
        self.SCHOOL = School.objects.create()
        self.TEACHER = Teacher.objects.create(school=self.SCHOOL)
        self.TEAM = Team.objects.create(teacher=self.TEACHER)
        self.student = Student.objects.create(id=1,firstName=self.FIRST_NAME,team=self.TEAM)

    def tearDown(self):
        self.student.delete()
        self.TEAM.delete()
        self.TEACHER.delete()
        self.SCHOOL.delete()

    def test_should_retrieve_correct_student(self):
        student = Student.objects.get(pk=1)
        self.assertEquals(student.firstName,self.FIRST_NAME)
        self.assertEquals(student.team,self.TEAM)

    def test_should_raise_integrity_error_for_empty_student(self):
        student = Student(team=self.TEAM)
        self.assertRaises(IntegrityError,student.save())

class TeamUnitTest(TestCase):

    def setUp(self):
        self.NAME = "BLUE"
        self.SCHOOL = School.objects.create()
        self.TEACHER = Teacher.objects.create(school=self.SCHOOL)
        self.team = Team.objects.create(id=1,name=self.NAME,teacher=self.TEACHER)

    def tearDown(self):
        self.team.delete()
        self.TEACHER.delete()
        self.SCHOOL.delete()

    def test_should_retrieve_correct_team(self):
        team = Team.objects.get(pk=1)
        self.assertEquals(team.name,self.NAME,"Team name does not match")
        self.assertEquals(team.teacher,self.TEACHER,"Teacher does not match")

    def test_should_raise_integrity_error_for_empty_team(self):
        team = Team(teacher=self.TEACHER)
        self.assertRaises(IntegrityError,team.save())

    def test_should_raise_integrity_error_for_name_greater_than_max(self):
        team = Team(teacher=self.TEACHER,name="thisistoomany")
        self.assertRaises(IntegrityError,team.save())


class TeacherUnitTest(TestCase):
    def setUp(self):
        self.FIRST_NAME = "Fname"
        self.LAST_NAME = "Lname"
        self.EMAIL = "TEST@TEST.COM"
        self.PASSWORD = MembershipService.encryptPassword(self.LAST_NAME,"PASSWORD")
        self.SCHOOL = School.objects.create()
        self.CLASS_NAME = "Test Class"
        self.teacher = Teacher.objects.create(id=1,firstName=self.FIRST_NAME,lastName=self.LAST_NAME,email=self.EMAIL,
                                              password=self.PASSWORD,school=self.SCHOOL,className=self.CLASS_NAME)

    def tearDown(self):
        self.teacher.delete()
        self.SCHOOL.delete()

    def test_should_retrieve_correct_teacher(self):
        teacher = Teacher.objects.get(pk=1)
        self.assertEquals(teacher.firstName,self.FIRST_NAME,"First name does not match")
        self.assertEquals(teacher.lastName,self.LAST_NAME,"Last name does not match")
        self.assertEquals(teacher.email,self.EMAIL,"Email does not match")
        self.assertEquals(teacher.password,self.PASSWORD,"Password does not match")
        self.assertEquals(teacher.school,self.SCHOOL,"School does not match")
        self.assertEquals(teacher.className,self.CLASS_NAME,"Class name does not match")

    def test_should_raise_integrity_error_for_empty_teacher(self):
        teacher = Teacher(school=self.SCHOOL)
        self.assertRaises(IntegrityError,teacher.save())


class SchoolUnitTest(TestCase):

    def setUp(self):
        self.NAME = "Test School"
        self.ADDRESS = "123 Lane"
        self.CITY = "New York"
        self.STATE = "NY"
        self.school = School.objects.create(id=1,name=self.NAME,address=self.ADDRESS,city=self.CITY,state=self.STATE)

    def tearDown(self):
        self.school.delete()

    def test_should_retrieve_correct_school(self):
        school = School.objects.get(pk=1)
        self.assertEquals(school.name,self.NAME,"School name does not match")
        self.assertEquals(school.address,self.ADDRESS,"Address does not match")
        self.assertEquals(school.city,self.CITY, "City does not match")
        self.assertEquals(school.state,self.STATE,"State does not match")

    def test_should_raise_integrity_error_for_empty_school(self):
        school = School()
        self.assertRaises(IntegrityError,school.save())

    def test_should_raise_integrity_error_for_state_length(self):
        self.school.state = "NEW YORK"
        self.assertRaises(IntegrityError,self.school.save())


# Views Unit Tests
class IndexUnitTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


# Functional Tests

class IndexFunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_should_load_index_page(self):
        #Open browser and go to site root
        self.browser.get(self.live_server_url)

        #Verify nav bar
        body = self.browser.find_element_by_tag_name('body')
        assert "MAPS" in body.text
        assert "INTERVIEWS" in body.text
        assert "ABOUT" in body.text
        assert "SIGN UP" in body.text
        assert "LOGIN" in body.text
        assert "City Digits: Local Lotto" in body.text

    def test_should_load_maps_view_when_map_is_clicked(self):
        #Open browser and go to site root
        self.browser.get(self.live_server_url)
        element = self.browser.find_element_by_link_text("MAP")
        element.click()
        div = self.browser.find_element_by_id('map')
        assert div.is_displayed() is True
        assert "TODO: MAP" in div.text

    def test_should_load_interviews_view_when_interview_is_clicked(self):
        #Open browser and go to site root
        self.browser.get(self.live_server_url)
        element = self.browser.find_element_by_link_text("INTERVIEWS")
        element.click()
        div = self.browser.find_element_by_id('interviews')
        assert div.is_displayed() is True
        assert "TODO: INTERVIEWS" in div.text

    def test_should_load_about_view_when_about_is_clicked(self):
        #Open browser and go to site root
        self.browser.get(self.live_server_url)
        element = self.browser.find_element_by_link_text("ABOUT")
        element.click()
        div = self.browser.find_element_by_id('about')
        assert div.is_displayed() is True
        assert "TODO: ABOUT" in div.text

    def test_should_load_tours_view_when_tours_is_clicked(self):
        #Open browser and go to site root
        self.browser.get(self.live_server_url)
        element = self.browser.find_element_by_link_text("TOURS")
        element.click()
        div = self.browser.find_element_by_id('tours')
        assert div.is_displayed() is True
        assert "TODO: TOURS" in div.text



