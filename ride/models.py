from decimal import Decimal
from django.db import models
from user.models import MyUser, Driver
from decimal import Decimal, ROUND_DOWN

class Ride(models.Model):
    CHOICES = (
        ('Peak', 'Peak'),
        ('Normal', 'Normal'),
        ('Smooth', 'Smooth'),
    )

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ride_user')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='ride_driver')
    pickup_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    distance = models.FloatField()
    type_of_ride = models.CharField(max_length=255, choices=CHOICES, default='Normal')
    base_fare = models.FloatField(blank=True, null=True)
    total_received = models.FloatField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    shared_with_friends = models.ManyToManyField(MyUser, related_name='shared_rides', blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination_location}"
    
    def save(self, *args, **kwargs):
        if not self.id:  # Check if it's a new instance
            if self.type_of_ride == 'Peak':
                self.base_fare = 1.5
            elif self.type_of_ride == 'Normal':
                self.base_fare = 1.3
            else:
                self.base_fare = 1.0
            
            total_received = Decimal(self.base_fare * self.distance).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
            self.total_received = float(total_received)
        super().save(*args, **kwargs)


