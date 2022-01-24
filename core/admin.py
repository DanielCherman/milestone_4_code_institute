from django.contrib import admin
from .models import ContactUs, CustomerQuery, Order, Portfolio

admin.site.register(ContactUs)
admin.site.register(Order)
admin.site.register(CustomerQuery)
admin.site.register(Portfolio)
