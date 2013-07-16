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
        assert "Maps" in body.text
        assert "Interviews" in body.text
        assert "About" in body.text
        assert "Sign Up" in body.text
        assert "Login" in body.text

