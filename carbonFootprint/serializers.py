from rest_framework import serializers
from .models import CarbonFootprint

class CarbonFootPrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonFootprint
        fields = '__all__'
