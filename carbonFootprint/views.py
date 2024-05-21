from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CarbonFootprint
from ride.models import Ride
from user.models import MyUser
from .serializers import CarbonFootPrintSerializer


@api_view(['GET'])
def get_carbon_footprint(request, pk):
    user = get_object_or_404(MyUser, id=pk)
    carbon_footprint = CarbonFootprint.objects.filter(user=user)
    serializer = CarbonFootPrintSerializer(carbon_footprint, many=True)
    return Response(serializer.data)
