from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

import views

# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^api/v1/notes/$',
        views.NoteList.as_view(),
        name='note-list'),

])
