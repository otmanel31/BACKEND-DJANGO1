from django.shortcuts import render
from rest_framework import viewsets
from users.models import *
from users.serializers import *
from rest_framework.response import Response

# Create your views here.
class NutriuserViewset(viewsets.ModelViewSet):
    queryset = Nutriuser.objects.all()
    serializer_class = NutriuserSerializer

class RepasViewset(viewsets.ModelViewSet):
    queryset =  Repas.objects.all()
    serializer_class = RepasSerializer

class ElementrepasViewset(viewsets.ModelViewSet):
    queryset = ElementRepas.objects.all()
    serializer_class = ElemenRepasSerializer
