from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

import views

# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^threads/$',
        views.ThreadList.as_view(),
        name='thread-list'),
    
    url(r'^threads/create/$',
        views.ThreadCreate.as_view(),
        name='thread-create'),
        
    url(r'^threads/(?P<pk>[0-9]+)/$',
        views.ThreadDetail.as_view(),
        name='thread-detail'),
        
    url(r'^threads/(?P<pk>[0-9]+)/notes/$',
        views.ThreadNotes.as_view(),
        name='thread-notes'),

    url(r'^threads/(?P<pk>[0-9]+)/join/$',
        views.ThreadJoin.as_view(),
        name='thread-join'),

    url(r'^threads/(?P<pk>[0-9]+)/leave/$',
        views.ThreadLeave.as_view(),
        name='thread-leave'),

])
