from decimal import Decimal
from django.db import models


# Create your models here.
# dev_3


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        decimal_places=2, default=Decimal("0"), max_digits=10
    )  # 99999999.99
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    image = models.ImageField(upload_to="upload/product/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_sale = models.BooleanField(default=False)  # dev_6
    sale_price = models.IntegerField(default=0)  # dev_6

    def __str__(self):
        return self.name
