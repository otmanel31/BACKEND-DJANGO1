from rest_framework import serializers
from aliments.models import *

class AlimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aliment
        fields = '__all__'

class NutrimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutriment
        fields = '__all__'

class NutdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutdata
        fields = '__all__'

class PortionalimentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Portionaliment
        fields = '__all__'
