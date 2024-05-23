from rest_framework import serializers
from .models import Promo

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'

class RedeemPromoSerializer(serializers.Serializer):
    promo_id = serializers.IntegerField()