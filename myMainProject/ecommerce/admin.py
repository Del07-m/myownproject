from django.contrib import admin
from .models import *  # Import the model


# Register your models here.


admin.site.register(Product) 
admin.site.register(Customer) 
admin.site.register(Order) 
admin.site.register(OrderItem) 