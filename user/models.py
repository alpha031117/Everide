from django.db import models

class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    profilePicture = models.ImageField(upload_to='profile_pictures/')
    friends = models.ManyToManyField('self', related_name='friends_list', blank=True)

    def __str__(self):
        return self.username

class Driver(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=20)
    rating = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    service_duration = models.DurationField()

    def __str__(self):
        return self.name
