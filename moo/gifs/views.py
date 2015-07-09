from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Gif
from .serializers import GifSerializer, GifSearchSerializer
from .giphy import query_giphy, random_giphy


class GifList(generics.ListCreateAPIView):
    """
    URL: /api/v1/gifs/
    Methods: GET
    Returns: List of gifs
    """
    queryset = Gif.objects.all()
    serializer_class = GifSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class GifDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/gifs/<pk>
    Methods: GET
    Returns: return teh gif
    """
    queryset = Gif.objects.all()
    serializer_class = GifSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class LikeGif(APIView):
    """
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, pk, format=None):
        user = self.request.user
        gif = Gif.objects.get(pk=pk)
        user.liked_gifs.add(gif)
        return Response({})


class UnlikeGif(APIView):
    """
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, pk, format=None):
        user = self.request.user
        gif = Gif.objects.get(pk=pk)
        user.liked_gifs.remove(gif)
        return Response({})




class GifSearch(APIView):
    """
    URL: /api/v1/gif/search/
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        serializer = GifSearchSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.data['query']
            results = query_giphy(query)
            response = {'results': results}
            return Response(response,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class GifRandom(APIView):
    """
    URL: /api/v1/gif/random/
    """
    def get(self, request):
        try:
            gif = random_giphy()
            response = {'results': gif}
            return Response(response,
                        status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
