from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from notes.models import Note
from notes.serializers import NoteSerializer

from .models import Thread
from .serializers import ThreadSerializer, ThreadStartSerializer


class ThreadList(generics.ListAPIView):
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


class ThreadCreate(generics.CreateAPIView):
    """
    URL: /api/v1/threads/create/
    Methods: GET, POST
    Returns: List of accounts, or creates a new account and adds
             the creator to the participants list
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadStartSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        user = self.request.user
        t = serializer.save()
        t.participants.add(user)


class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/threads/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Handle an individual thread object
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class ThreadNotes(generics.ListAPIView):
    """
    URL: /api/v1/threads/<pk>/notes/
    Methods: GET
    Returns: Pull all notes in the threads
    """
    serializer_class = NoteSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        thread = get_object_or_404(Thread, pk=self.kwargs['pk'])
        return Note.objects.filter(thread=thread)
