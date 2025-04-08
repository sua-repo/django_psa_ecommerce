from django.db import models

from store.models import Product

# Create your models here.


# dev_24
class Order(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    amount_paid = models.PositiveBigIntegerField(default=0)  # 계산 총액
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Order - {str(self.id)}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.PositiveBigIntegerField(default=1)  # 수량
    price = models.PositiveBigIntegerField(default=0)  # 가격

    def __str__(self):
        return f"Order - {str(self.id)}"

    def get_cost(self):
        return self.price * self.quantity
