# Django modules
from django.db import models

from catalog.models import *

class User(models.Model):
    """
    Represent a customer in the system
    """
    name = models.TextField()
    phone = models.IntegerField()
    email = models.TextField(unique=True)
    password = models.TextField()

    def __str__(self):
        return self.email
    
class Addresses(models.Model):
    """
    Represent user's address
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="address")
    street = models.TextField()
    appartment = models.IntegerField()

class Order(models.Model):
    """
    Represent a customer order
    """
    STATUS_CHOICES = [
        ("new", "New"),
        ("confirmed", "Confirmed"),
        ("delivering", "Delivering"),
        ("done", "Done")
    ]
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name="order")
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE, related_name="order")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="order")
    status = models.TextField(choices=STATUS_CHOICES, default="new")
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    discount_total = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Order {self.pk} by {self.user_id.email}"
    
class OrderItem(models.Model):
    """
    Represent an item within an order
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="item")
    item_name = models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    line_total = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.item_name}"
    
class OrderItemOption(models.Model):
    """
    Represent an option selected for a specific order item
    """
    order_item_id = models.ForeignKey(OrderItem,on_delete=models.CASCADE,related_name="options")
    option_name = models.TextField()
    option_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.option_name} + {self.option_price}"
    
class PromoCode(models.Model):
    """
    Represent a promocode
    """
    discount_code = models.TextField(unique=True)
    discount_percent = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.discount_code
    
class OrderPromo(models.Model):
    """
    Represent a promo taht applied to an order
    """
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="promo")
    promo_id = models.OneToOneField(PromoCode, on_delete=models.CASCADE, related_name="order")
    applied_amount = models.IntegerField()

    def __str__(self):
        return f"{self.promo_id.discount_code} applied to order{self.order_id}"
    
    
    
