from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EWallet
from user.models import MyUser
from .serializers import EWalletSerializer

# Create your views here.

@api_view(['GET'])
def view_wallet(request, pk):
    user = get_object_or_404(MyUser, id=pk)
    wallet = get_object_or_404(EWallet, user=user)
    serializer = EWalletSerializer(wallet, many=False)
    return Response(serializer.data)