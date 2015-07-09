from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from gifs import views


# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^gif/search/$',
        views.GifSearch.as_view(),
        name='gif-search'),
    
    url(r'^gif/random/$',
        views.GifRandom.as_view(),
        name='gif-random'),
])