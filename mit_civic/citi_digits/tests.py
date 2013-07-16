"""
This file contains both unit tests and functional tests for the citi digits application. These will run
when you run "manage.py test".

"""

from django.test import LiveServerTestCase
from selenium import webdriver

class IndexTest(LiveServerTestCase):

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
        self.assertIn('Maps',body.text)

