# -*- coding: utf-8 -*-
#!/usr/bin/env python

# ############################################################################
# Copyright  : (C) 2014 by MHComm. All rights reserved
#
# Name       : views.py
"""
   Summary    :  Views for nutrieduc ressources
"""
# #############################################################################
from __future__ import absolute_import
from __future__ import unicode_literals

__author__ = "Jean-Christophe Buisson"
__copyright__ = "(C) 2014 by MHComm. All rights reserved"
__email__ = "info@mhcomm.fr"

import logging

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from nutrieduc import serializers, models, nutrition
from mhuser.models import User
#from mhuser import models as usr_models

logger = logging.getLogger('quesper.nutri')


# viewset for viewing and editing Aliment instances
class AlimentViewSet(ModelViewSet):
    
    model = models.Aliment
    serializer_class = serializers.AlimentSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = models.Aliment.objects.all()


# viewset for viewing and editing PortionAliment instances associated to Aliment of id <alimId>
class PortionAlimentViewSet(ModelViewSet):

    permission_classes = (permissions.AllowAny,)
    model = models.PortionAliment
    serializer_class = serializers.PortionAlimentSerializer

    def get_queryset(self):
        return models.PortionAliment.objects.filter(aliment=self.kwargs.get('alimId'))

#
# viewset for viewing and editing Nutriment instances
#
class NutrimentViewSet(ModelViewSet):

    permission_classes = (permissions.AllowAny,)
    model = models.Nutriment
    serializer_class = serializers.NutrimentSerializer
    queryset = models.Nutriment.objects.all()


#
# viewset for viewing and editing PortionAliment instances associated to Aliment of id <alimId>
#
class NutDataViewSet(ModelViewSet):

    permission_classes = (permissions.AllowAny,)
    model = models.NutData
    serializer_class = serializers.NutDataSerializer

    def get_queryset(self):
        return models.NutData.objects.filter(aliment=self.kwargs.get('alimId'))



####################      custom class-based views       #####################


class SearchView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.DATA
        # exclude brand food
        queryset = models.Aliment.objects.filter(shrt_desc__icontains=data['search']).exclude(brand=True)
        serializer = serializers.AlimentSerializer(queryset, many=True)
        return Response(serializer.data)

