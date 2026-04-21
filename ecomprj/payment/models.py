from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    delivery_full_name = models.CharField(max_length=100)
    delivery_email = models.CharField(max_length=100)
    delivery_address_line1 = models.CharField(max_length=255)
    delivery_address_line2 = models.CharField(max_length=255, blank=True, null=True)
    delivery_city = models.CharField(max_length=100)
    delivery_state = models.CharField(max_length=100, null=True)
    delivery_zip_code = models.CharField(max_length=20, null=True)
    delivery_country = models.CharField(max_length=100)
    delivery_phone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return f"Shipping Addresses - {str(self.id)}"
    

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    shipping_address = models.EmailField(max_length=2500)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=3)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped=models.BooleanField(default=False)


    def __str__(self):
        return f"Order - {self.id}"

class OrderItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"OrderItem - {self.id}"
