from time import timezone

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.product.price * self.quantity

    def create_rental_log(self):
        rental_log = RentalLog.objects.create(
            user=self.user,
            product=self.product,
            rental_cost=self.product.price * self.quantity,
            rental_amount=self.quantity,
            rental_unit_price=self.product.price
        )
        return rental_log

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.quantity}"


class RentalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rental_time = models.DateTimeField(auto_now_add=True)
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2)
    rental_amount = models.PositiveIntegerField()
    rental_unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Add other fields as needed

    class Meta:
        ordering = ['-rental_time']
