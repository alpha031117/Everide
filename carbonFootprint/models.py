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
    total_distance = models.FloatField(default=0.0)
    tier = models.CharField(max_length=255, choices=tier_choices, default='No Tier')
    footprint = models.FloatField()

    def __str__(self):
        return f"Carbon footprint for {self.user.username}"
    
    def save(self, *args, **kwargs):
        # Determine tier based on total distance traveled
        if self.total_distance >= 3000:
            self.tier = 'Gold'
        elif self.total_distance >= 1000:
            self.tier = 'Silver'
        elif self.total_distance >= 100:
            self.tier = 'Bronze'
        else:
            self.tier = 'No Tier'
            
        super().save(*args, **kwargs)