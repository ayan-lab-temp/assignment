from django.db import models
from users.models import User
from restraunts.models import MenuItem, Restuarent
from django.core.validators import MinValueValidator

# Create your models here.
class Order(models.Model):
    PAYMENT_PENDING = 'p'
    PAYMENT_COMPLETED = 'c'
    PAYMENT_FAILED = 'f'
    
    PAYMENT_CHOICES = [
        (PAYMENT_PENDING, 'pending'),
        (PAYMENT_COMPLETED, 'completed'),
        (PAYMENT_FAILED, 'failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    restaurant = models.ForeignKey(Restuarent, on_delete=models.PROTECT, related_name='orders')
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)