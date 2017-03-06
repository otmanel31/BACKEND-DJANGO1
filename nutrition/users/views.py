from django.shortcuts import render
from rest_framework import viewsets
from users.models import *
from users.serializers import *
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.views import APIView

# Create your views here.
class NutriuserViewset(viewsets.ModelViewSet):
    queryset = Nutriuser.objects.all()
    serializer_class = NutriuserSerializer


class RepasViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)  # SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Repas.objects.all()
    serializer_class = RepasSerializer
    print(queryset)


class ElementrepasViewset(viewsets.ModelViewSet):
    queryset = ElementRepas.objects.all()
    serializer_class = ElemenRepasSerializer

class TotalCalorique(APIView):
    def post(self):
        pass