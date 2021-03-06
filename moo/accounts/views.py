from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer, AccountSearchSerializer

from threads.models import Thread
from threads.serializers import ThreadSerializer

from gifs.models import Gif
from gifs.serializers import GifSerializer


class AccountList(generics.ListAPIView):
    """
    URL: /api/v1/accounts/
    Methods: GET
    Returns: List of accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountCreate(generics.CreateAPIView):
    """
    URL: /api/v1/accounts/create/
    Methods: POST
    Returns: Creates an account
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = set()
    permission_classes = set()


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    URL: /api/v1/accounts/<pk>/
    Methods: GET, PUT, DELETE
    Returns: Handle an individual account object
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class AccountThreads(generics.ListAPIView):
    """
    URL: /api/v1/accounts/<pk>/threads/
    Methods: GET
    Returns: List all the threads of the user
    """
    serializer_class = ThreadSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        user = get_object_or_404(Account, pk=self.kwargs['pk'])
        return Thread.objects.filter(participants=user)


class AccountFriends(generics.ListAPIView):
    """
    URL: /api/v1/accounts/<pk>/friends/
    Methods: GET
    Returns: List all the friends of the user
    """
    serializer_class = AccountSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        user = get_object_or_404(Account, pk=self.kwargs['pk'])
        return user.friends.all()


class AccountLikedGifs(generics.ListAPIView):
    """
    URL: /api/v1/accounts/<pk>/gifs/
    Methods: GET
    Returns: 
    """
    serializer_class = GifSerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        user = get_object_or_404(Account, pk=self.kwargs['pk'])
        return user.liked_gifs.all()


class FriendAccount(APIView):
    """
    URL: /api/v1/accounts/<pk>/add/friend/
    Methods: POST
    Returns: Make a user a friend
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, format=None):
        me = request.user
        target = Account.objects.get(pk=pk)

        if target == me:
            return Response(status=status.HTTP_409_CONFLICT)
        
        me.add_friend(target)
        return Response(AccountSerializer(target).data, 
                        status=status.HTTP_200_OK)


class SearchAccount(APIView):
    """
    URL: /api/v1/accounts/search/
    Methods: POST
    Returns: Search for a user by username
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        serializer = AccountSearchSerializer(data=request.data)
        results = []

        if serializer.is_valid():
            if serializer.data['username']:
                try:
                    a = Account.objects.get(username=serializer.data['username'])
                    results.append(AccountSerializer(a).data)
                    return Response(results, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response(status=status.HTTP_404_NOT_FOUND)
        
            elif serializer.data['number']:
                try:
                    for number in serializer.data['number']:
                        a = Account.objects.get(phonenumber=number)
                        results.append(AccountSerializer(a).data)
                    return Response(results, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response(status=status.HTTP_404_NOT_FOUND)

            
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class MeDetail(APIView):
    """
    URL: /api/v1/me/
    Methods: GET
    Returns: Account object of the authenticated user making the request.
    """
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        me = request.user
        serializer = AccountSerializer(me, context={'request': request})
        return Response(serializer.data)
