from rest_framework import serializers
from .models import Ride

class MyRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'

class FootprintSerializer(serializers.ModelSerializer):
    footprint = serializers.FloatField()