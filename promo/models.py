from django.db import models
from user.models import MyUser

class Promo(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=255, default="")
    amount_spend = models.IntegerField(default=0)
    reward_amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class RedeemedPromo(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='redeemed_promos')
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} redeemed {self.promo.title}"
