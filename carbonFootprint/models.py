from django.db import models
from user.models import MyUser

class CarbonFootprint(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='carbon_footprint')
    footprint = models.FloatField()

    def __str__(self):
        return f"Carbon footprint for {self.user.username}"
