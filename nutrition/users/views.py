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

def get_auth_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        print('ok PASSAFE')
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            return redirect('/api/aliments/', request)

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
