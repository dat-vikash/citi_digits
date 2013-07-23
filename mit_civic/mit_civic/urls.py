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
        url(r'^interview/new/$', 'citi_digits.views.interview_select', name='interview_select'),

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
