from django.db import models
from user.models import MyUser, Driver

class Ride(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    base_fare = models.FloatField()
    extra_tips = models.FloatField()
    total_received = models.FloatField()
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    shared_with_friends = models.ManyToManyField(MyUser, related_name='shared_rides', blank=True)

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination}"
    
class BookingHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='booking_history')
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking history for {self.user.username}"

