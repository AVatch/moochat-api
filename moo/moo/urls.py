"""moo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import views

VERSION = 'v1'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/' + VERSION + '/$', views.api_root),

    url(r'^api/' + VERSION + '/', include('accounts.urls')),
    url(r'^api/' + VERSION + '/', include('threads.urls')),
    url(r'^api/' + VERSION + '/', include('notes.urls')),
    url(r'^api/' + VERSION + '/', include('gifs.urls')),
)

urlpatterns += staticfiles_urlpatterns()
