from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

import views

# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^api/v1/threads/$',
        views.ThreadList.as_view(),
        name='thread-list'),
    
    url(r'^api/v1/threads/create/$',
        views.ThreadCreate.as_view(),
        name='thread-create'),
        
    url(r'^api/v1/threads/(?P<pk>[0-9]+)/$',
        views.ThreadDetail.as_view(),
        name='thread-detail'),
        
    url(r'^api/v1/threads/(?P<pk>[0-9]+)/notes/$',
        views.ThreadNotes.as_view(),
        name='thread-notes'),

])
