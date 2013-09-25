from citi_digits.models import CityDigitsUser, Interview, Teacher, Tour, InterviewComment

__author__ = 'vikash'

from django.contrib import admin

admin.site.register(CityDigitsUser)
admin.site.register(Interview)
admin.site.register(Teacher)
admin.site.register(Tour)
admin.site.register(InterviewComment)