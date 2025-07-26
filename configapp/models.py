from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    muddat = models.DateTimeField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    company_name = models.CharField(max_length=40)
    address = models.TextField()
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name


class Orders(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    required_date = models.DateTimeField()
    shipped_date = models.DateTimeField()