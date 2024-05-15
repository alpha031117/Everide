from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyUserSerializer, DriverSerializer, LoginSerializer, CreateMyUserSerializer
from .models import MyUser, Driver

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
def create_user(request):
    serializer = CreateMyUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_driver(request):
    serializer = DriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    