from citi_digits.models import CityDigitsUser, Interview, Teacher, Tour, InterviewComment,InterviewRetailer, InterviewPlayer

__author__ = 'vikash'

from django.contrib import admin

def getStudentName(model):
    """
      Return the students name to aide in display.
    """
    return model.student.firstName

def getInterviewTitle(model):
    """
      Returns the interview title
    """
    if model.interviewType == "RETAILER":
        return model.getInterview().storeName

    if model.interviewType == "PLAYER":
        return model.getInterview().firstName


class InterviewAdmin(admin.ModelAdmin):
    list_display = ['id',getInterviewTitle, getStudentName, 'interviewType','created_at']
    ordering = ['created_at']

class InterviewRetailerAdmin(admin.ModelAdmin):
    list_display = ['id','storeName']

class InterviewPlayerAdmin(admin.ModelAdmin):
    list_display = ['id','firstName']

admin.site.register(CityDigitsUser)
admin.site.register(Interview,InterviewAdmin)
admin.site.register(Teacher)
admin.site.register(Tour)
admin.site.register(InterviewComment)
admin.site.register(InterviewRetailer,InterviewRetailerAdmin)
admin.site.register(InterviewPlayer,InterviewPlayerAdmin)