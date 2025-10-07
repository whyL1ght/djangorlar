# Django modules
from django.db import models

class Restaurant(models.Model):
    """
    Represents a restaurant with name and rating
    """
    name = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    """
    Represent a food or drink item available at restaurant
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menu_items")
    is_available = models.BooleanField(default=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

class Category(models.Model):
    """
    Represent all category of menu items
    """
    name = models.TextField()

    def __str__(self):
        return self.name
    
class ItemCategory(models.Model):
    """
    Represent an item category
    """
    item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="item_category")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="item_category")
    position = models.IntegerField()

        
class Option(models.Model):
    """
    Represent selectable option for menu items
    """
    name = models.TextField()

    def __str__(self):
        return self.name
    
class ItemOption(models.Model):
    """
    Associates a menu item with one of possible option
    """
    item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="item_options")
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="item_options")
    price_delta = models.DecimalField(max_digits=10, decimal_places=2)
    is_default = models.BooleanField(default=False)

    



