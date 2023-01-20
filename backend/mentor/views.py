from argparse import Action
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action


# Create your views here.

from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

from .serializers import MentorSerializer, TableSerializer
from .models import Mentor
from rest_framework.response import Response
from django.http.response import HttpResponse

from rest_framework import permissions


from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.views.application import ApplicationDetail


# class MentorsViewSet(ProtectedResourceView, viewsets.ModelViewSet):
class MentorsViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all().order_by('id')
    serializer_class = MentorSerializer
    # permission_classes = [permissions.IsAuthenticated,TokenHasScope]
    # permission_classes = [TokenHasScope]
    # required_scopes = []


class TableViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all().order_by('id')
    serializer_class = TableSerializer
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    # permission_classes = [TokenHasReadWriteScope]

    def list(self, request):
        queryset = Mentor.objects.all().order_by('id')
        serializer = TableSerializer(queryset, many=True)

        final = {"mentors":serializer.data}

        return Response(final)
