from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    PRODUCT_STATUS = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('out_of_stock', 'Out of Stock'),
        ('discontinued', 'Discontinued'),
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default='available')
    
    
# Create your models here.
    def __str__(self):
        return self.name

class productReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Certificate for {self.product.name}"