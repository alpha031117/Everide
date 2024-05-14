from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MyUserSerializer
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
    serializer = MyUserSerializer(driver, many=True)
    return Response(serializer.data)