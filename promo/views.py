from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Promo, RedeemedPromo
from carbonFootprint.models import CarbonFootprint
from wallet.models import EWallet
from user.models import MyUser
from .serializers import PromoSerializer, RedeemPromoSerializer
from rest_framework import status


@api_view(['GET'])
def view_promo(request):
    promo = Promo.objects.all()
    serializer = PromoSerializer(promo, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
def allocate_rewards(request, user):
    serializer = RedeemPromoSerializer(data=request.data)
    
    if serializer.is_valid():
        promo_id = serializer.validated_data['promo_id']
        promo = get_object_or_404(Promo, id=promo_id)
        
        user = get_object_or_404(MyUser, id=user)
        carbon_footprint = get_object_or_404(CarbonFootprint, user=user)
        
        if carbon_footprint.footprint < promo.amount_spend:
            return Response({"message": "User does not qualify for this reward."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Deduct the required carbon footprint
        carbon_footprint.footprint -= promo.amount_spend
        carbon_footprint.save()
        
        # Allocate the reward to the user's e-wallet
        ewallet, created = EWallet.objects.get_or_create(user=user)
        ewallet.amount += promo.reward_amount
        ewallet.save()
        
        # Record the redeemed promo
        RedeemedPromo.objects.create(user=user, promo=promo)
        
        return Response({"detail": f"Promo '{promo.title}' redeemed successfully. RM{promo.reward_amount} allocated to the wallet."}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

