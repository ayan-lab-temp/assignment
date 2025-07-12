from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.PositiveIntegerField(null=True)
    