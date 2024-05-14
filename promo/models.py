from django.db import models

class Promo(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.FloatField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.code
