#from django.http.response import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework import viewsets
from . models import tanks
from . serializers import tanksSerializer

class tankList(viewsets.ModelViewSet):
    queryset = tanks.objects.all()
    serializer_class = tanksSerializer