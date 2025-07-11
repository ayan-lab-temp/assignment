from django.db import models
from django.core.validators import MinValueValidator
from users.models import User

# Create your models here.

class Restuarent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.PositiveSmallIntegerField(null=True)

    
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    restaurant = models.ForeignKey(Restuarent, on_delete=models.CASCADE)
    

    
    
    
