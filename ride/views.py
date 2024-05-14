from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MyRideSerializer
from .models import Ride 
from user.models import MyUser

@api_view(['GET'])
def get_ride(request):
    ride = Ride.objects.all()
    serializer = MyRideSerializer(ride, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_ride(request, pk):
    try:
        user_obj = MyUser.objects.get(id=pk)
        rides = Ride.objects.filter(user=user_obj)
        serializer = MyRideSerializer(rides, many=True)
        return Response(serializer.data)
    except MyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_ride(request):
    serializer = MyRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
