from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from .models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListAPIView):
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
 