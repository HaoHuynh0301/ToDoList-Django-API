from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from . import models
from .serializers import ToDoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class ToDoView(generics.ListAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetailView(generics.RetrieveAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = ToDoSerializer

