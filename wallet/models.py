from django.db import models
from user.models import MyUser

class EWallet(models.Model):

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='ewallet')
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f"EWallet for {self.user.username}"