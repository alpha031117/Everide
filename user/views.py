from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyUserSerializer, DriverSerializer, LoginSerializer
from .models import MyUser, Driver
from carbonFootprint.models import CarbonFootprint
from wallet.models import EWallet
from django.core.files.base import ContentFile
from base64 import b64decode

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/ride',
            'Method': 'GET',
            'Body': None,
            'Description': 'Retrieve ride history'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def get_user(request):
    user = MyUser.objects.all()
    serializer = MyUserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_driver(request):
    driver = Driver.objects.all()
    serializer = DriverSerializer(driver, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    data = request.data

    # Handling friends
    friend_ids = data.get('friends', [])
    friends = MyUser.objects.filter(id__in=friend_ids)

    user = MyUser.objects.create(
        username=data['username'], 
        email=data['email'], 
        password=data['password'], 
        phoneNumber=data['phoneNumber']
    )

    user.friends.add(*friends)  # Add friends to the user

    CarbonFootprint.objects.create(
        user=user,
        tier='No Tier',
        footprint=0
    )

    EWallet.objects.create(
        user=user,
        amount=0.0
    )

    serializer = MyUserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def updateUser(request, pk):
    try:
        user = MyUser.objects.get(pk=pk)
    except MyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MyUserSerializer(user, data=request.data, partial=True)  # Pass request data to serializer, allowing partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = MyUser.objects.get(id=pk)
    user.delete()

    return Response('User deleted')


@api_view(['POST'])
def createDriver(request):
    data = request.data

    driver = Driver.objects.create(
        name=data['name'], 
        car_model=data['car_model'], 
        plate_number=data['plate_number'], 
        rating=data['rating'], 
        active=data['active'], 
        service_duration_year=data['service_duration_year']
    )

    serializer = DriverSerializer(driver, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_friend(request):
    if request.method == 'POST':
        user = MyUser.objects.get(username=request.data['username'])
        friend = MyUser.objects.get(username=request.data['friend'])
        user.friends.add(friend)
        return Response(status=status.HTTP_200_OK)
    