from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .choices import STATUS, DESIGN_TYPE, UNIT_TYPE

class ContactUs(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class CustomerQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_request')
    title = models.CharField(max_length=250)
    design_type = models.CharField(max_length=15, choices=DESIGN_TYPE)
    width = models.FloatField(validators=[MinValueValidator(0.0)])
    height = models.FloatField(validators=[MinValueValidator(0.0)])
    unit = models.CharField(max_length=5, choices=UNIT_TYPE)
    sketch = models.ImageField(upload_to='uploads/sketch', null=True, blank=True)
    description = models.TextField()
    description_message = models.TextField(null=True, blank=True)
    final_price = models.FloatField(validators=[MinValueValidator(0.0)], null=True, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return self.title


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_buyer')
    title = models.CharField(max_length=250)
    description = models.TextField()
    final_price = models.FloatField(validators=[MinValueValidator(0.0)])
    delivery_file = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=20, choices=STATUS, default='In_Progress')

    def __str__(self):
        return self.title + " " + str(self.status)


class Portfolio(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title