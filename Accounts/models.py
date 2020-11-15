from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-date_created']
