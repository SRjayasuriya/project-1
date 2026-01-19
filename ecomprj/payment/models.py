from django.db import models
from django.contrib.auth.models import User

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

    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return f"Shipping Addresses - {str(self.id)}"