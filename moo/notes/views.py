from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from .models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    """
    URL: /api/v1/notes/
    Methods: GET
    Returns: List of notes
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
 
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/notes/<pk>
    Methods: GET
    Returns: List of notes
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
