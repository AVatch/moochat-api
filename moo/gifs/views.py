from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from gifs.serializers import GifSearchSerializer
from gifs.giphy import query_giphy, random_giphy

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
            print "|"*50
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
