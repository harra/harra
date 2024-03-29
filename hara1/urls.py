# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'hara1.views.index'), 
   url(r'^login_user/$', 'hara1.views.login_user'),
   url(r'^services/$', 'hara1.views.services'),
   url(r'^system_manage/$', 'hara1.views.system_manage'),
   url(r'^reports/$', 'hara1.views.reports'),
   
   url(r'^logout_user/$', 'hara1.views.logout_user'),

    # url(r'^$', 'hara1.views.home', name='home'),
    # url(r'^hara1/', include('hara1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'static'),
    )