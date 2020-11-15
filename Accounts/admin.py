from django.contrib import admin
from . models import *


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')


admin.site.register(Customer, CustomerAdmin)
