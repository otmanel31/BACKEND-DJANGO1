from rest_framework import serializers
from users.models import *

class NutriuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutriuser
        fields = '__all__'

class RepasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repas
        fields = '__all__'

class ElemenRepasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementRepas
        fields = '__all__'
