from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from .models import Thread
from .serializers import ThreadSerializer


class ThreadList(generics.ListCreateAPIView):
    """
    URL: /api/v1/threads/
    Methods: GET, POST
    Returns: List of accounts, or creates a new account and adds
             the creator to the participants list
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        user = self.request.user
        t = serializer.save()
        t.participants.add(user)
