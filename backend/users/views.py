import base64
import re

from django.contrib.auth import authenticate
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from users.models import User
from users.serializers import UserSerializer


class Users(ListAPIView):
    """
    List all code operations, or create a new record.
    """
    serializer_class = UserSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    queryset = User.objects.all()
    permission_classes= [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class Login(ObtainAuthToken):
    
    def _process_authorization(self, token:str):
        auth_pair = re.search('Basic (.*)', token).group(1)
        byte_str = str.encode(auth_pair)
        decoded = base64.b64decode(byte_str)
        username, pwd = decoded.decode().split(':')
        return username, pwd
        
    
    def _check_user(self, username:str, pwd:str):
        user = authenticate(username=username, password=pwd)
        if user is None:
            return HttpResponseForbidden()
        return user        
    
    def post(self, request, *args, **kwargs):
        breakpoint();
        username, pwd = self._process_authorization(token=request.headers.get('Authorization'))
        user = self._check_user(username=username, pwd=pwd)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })
    def options(self, request, *args, **kwargs):
        breakpoint()
        return Response(status=204, headers={
            "Access-Control-Allow-Methods": 'POST, GET, OPTIONS, DELETE',
            "Access-Control-Allow-Origin": "*",
        })
        
class Logout(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes= [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({'success':'User deauthenticated'})