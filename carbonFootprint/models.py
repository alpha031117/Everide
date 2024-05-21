from django.db import models
from user.models import MyUser

class CarbonFootprint(models.Model):
    tier_choices = (
        ('No Tier', 'No Tier'),
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    )
        
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='carbon_footprint')
    tier = models.CharField(max_length=255, choices=tier_choices, default='No Tier')
    footprint = models.FloatField()

    def __str__(self):
        return f"Carbon footprint for {self.user.username}"
