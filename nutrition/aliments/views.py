from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from aliments.models import *
from aliments.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.

class ListAliments(APIView):
    def post(self, request, nutr_no):
        datas = request.data
        print(datas)
        total = 0
        moyenne = 0
        for data in datas:
            nut_data = Nutdata.objects.get(aliment_id = data, nutriment_id=nutr_no)
            print('my nutdata', nut_data.val)
            total += float(nut_data.val)
            moyenne = (total/len(data))
        return Response(moyenne)

     #data = liste d'id alilmebnt et nutr_no id d'un nutriment
    #a partir de l id_nutriment fournit trouver les nutdata de ces aliments


class AlimentViewSet(viewsets.ModelViewSet):
    #authentication_classes = (SessionAuthentication, )#SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticated,) #TokenAuthentication

    queryset = Aliment.objects.all()
    serializer_class = AlimentSerializer

    filter_fields = ('shrt_desc', 'long_desc', 'pîct')

    def get_queryset(self):
        qs = self.queryset
        search = self.request.query_params.get('search', None)
        if search:
            qs = qs.filter(shrt_desc__icontains = search)
        return qs

class NutrimentViewSet(viewsets.ModelViewSet):
    queryset = Nutriment.objects.all()
    serializer_class = NutrimentSerializer

class NutdataViewSet(viewsets.ModelViewSet):
    queryset = Nutdata.objects.all()
    serializer_class = NutdataSerializer

class PortionalimentViewSet(viewsets.ModelViewSet):
    queryset = Portionaliment.objects.all()
    serializer_class = PortionalimentSerializer

    def get_queryset(self):
        queryset = self.queryset
        aliment_id = self.request.query_params.get('aliment_id', None)
        if aliment_id is not None:
            queryset = queryset.filter(aliment_id=aliment_id)
        return queryset