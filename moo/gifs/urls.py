from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from gifs import views


# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^gifs/$',
        views.GifList.as_view(),
        name='gif-list'),
    
    url(r'^gifs/(?P<pk>[0-9]+)/$',
        views.GifDetail.as_view(),
        name='gif-detail'),

    url(r'^gifs/(?P<pk>[0-9]+)/like/$',
        views.LikeGif.as_view(),
        name='gif-like'),

    url(r'^gifs/(?P<pk>[0-9]+)/unlike/$',
        views.UnlikeGif.as_view(),
        name='gif-unlike'),

    url(r'^gif/search/$',
        views.GifSearch.as_view(),
        name='gif-search'),
    
    url(r'^gif/random/$',
        views.GifRandom.as_view(),
        name='gif-random'),
])