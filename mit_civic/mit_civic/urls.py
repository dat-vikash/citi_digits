from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', 'citi_digits.views.index', name='index'),
        url(r'^signup/$', 'citi_digits.views.signUp', name='signup'),
        url(r'^login/$', 'citi_digits.views.login', name='login'),
        url(r'^logout/$', 'citi_digits.views.logout', name='logout'),
        url(r'^map/nav/$', 'citi_digits.views.mapNavigation', name='mav_nav'),
        url(r'^interview/new/$', 'citi_digits.views.interviewSelect', name='interview_select'),
        url(r'^interview/player/$', 'citi_digits.views.interviewPlayer', name='interview_player'),
        url(r'^interview/retailer/$', 'citi_digits.views.interviewRetailer', name='interview_retailer'),
        url(r'^popup/(?P<layer>.+)/(?P<neighborhood>.+)/(?P<perin>.+)/(?P<dol>.+)/(?P<sale>.+)/(?P<win>.+)/(?P<income>.+)/(?P<netwin>.+)/$','citi_digits.views.popup',name='popup'),
        url(r'^mathematical_explain/(?P<neighborhood>.+)/(?P<spent>.+)/(?P<income>.+)/$', 'citi_digits.views.mathExplain', name='math_explaination'),
        url(r'^interview/geoJson/$', 'citi_digits.views.loadGeoJsonInterviews', name='geojson'),
        url(r'^interview/list/(?P<offset>.+)/$', 'citi_digits.views.interviewList', name='interview_list'),
        url(r'^interview/(?P<id>.+)/comment/$', 'citi_digits.views.comment', name='comments'),
        url(r'^interview/(?P<id>.+)/$', 'citi_digits.views.interviewDetails', name='interview_details'),
        url(r'^tour/new/$', 'citi_digits.views.tour', name='add_tour'),
        url(r'^tour/preview/$', 'citi_digits.views.tourPreview', name='tour_preview'),


    # Examples:
    # url(r'^$', 'mit_civic.views.home', name='home'),
    # url(r'^mit_civic/', include('mit_civic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += (
        url(r'^media/(.*)$', 'django.views.static.serve',
                    {'document_root': settings.MEDIA_ROOT}),
    )
