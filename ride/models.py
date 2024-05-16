from decimal import Decimal
from django.db import models
from user.models import MyUser, Driver
from decimal import Decimal, ROUND_DOWN

class Ride(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver')
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    base_fare = models.FloatField()
    distance = models.FloatField()
    total_received = models.FloatField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    shared_with_friends = models.ManyToManyField(MyUser, related_name='shared_rides', blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Corrected invocation of super()

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination}"
    
    def save(self, *args, **kwargs):
        if not self.id:  # Check if it's a new instance
            total_received = Decimal(self.base_fare * self.distance).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
            self.total_received = total_received
        super().save(*args, **kwargs)


