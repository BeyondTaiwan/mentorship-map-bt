from logging import raiseExceptions
from django.conf import settings
from django.contrib.auth import login

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UsersSerializer
from .models import User

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UsersSerializer

class UserLoginAPI(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        user = User.authenticate(User, request, token)
        if user is None:
            raise 
        login(request, user)
        return Response({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        })

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')