"""
This file contains both unit tests and functional tests for the citi digits application. These will run
when you run "manage.py test".

"""

from django.test import LiveServerTestCase
from unittest import TestCase
from selenium import webdriver
from django.test import Client


# Unit Tests
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



