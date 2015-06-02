from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

import views

# API endpoints
urlpatterns = format_suffix_patterns([

    url(r'^api/v1/accounts/$',
        views.AccountList.as_view(),
        name='account-list'),

    url(r'^api/v1/accounts/create/',
        views.AccountCreate.as_view(),
        name='account-create'),

    url(r'^api/v1/accounts/(?P<pk>[0-9]+)/$',
        views.AccountDetail.as_view(),
        name='account-detail'),
        
   url(r'^api/v1/accounts/(?P<pk>[0-9]+)/threads/$',
        views.AccountThreads.as_view(),
        name='account-threads'),
   
   url(r'^api/v1/accounts/(?P<pk>[0-9]+)/friends/$',
        views.AccountFriends.as_view(),
        name='account-friends'),
        
   url(r'^api/v1/accounts/(?P<pk>[0-9]+)/add/friend/$',
        views.FriendAccount.as_view(),
        name='account-add-friend'),

    url(r'^api/v1/me/$',
        views.MeDetail.as_view(),
        name='me-detail'),
])

# Get the auth token for the user
urlpatterns += [
    url(r'^api/v1/api-token-auth/', rest_views.obtain_auth_token)
]
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api/v1/api-auth/', include('rest_framework.urls',
                                      namespace='rest_framework')),
]