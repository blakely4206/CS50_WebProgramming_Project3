from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length =2,default="AR")
    zip_code = models.CharField(max_length=5)

class Pizza_Size(models.Model):
    size = models.CharField(max_length=20)
    
    def __str__(self):
        return self.size

class Pizza_Style(models.Model):
    style = models.CharField(max_length=20)
    
    def __str__(self):
        return self.style
    
class Pizza_Topping_Type(models.Model):
    topping_type = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    
    def __str__(self):
        return self.topping_type
    
class Topping(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
class Pizza_Type(models.Model):
    size = models.ForeignKey(Pizza_Size, on_delete=models.CASCADE)
    style = models.ForeignKey(Pizza_Style, on_delete=models.CASCADE)
    topping_type = models.ForeignKey(Pizza_Topping_Type, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    
    def __str__(self):
        pizza_string = "{0} {1} {2} ${3}"
        return pizza_string.format(self.size, self.style, self.topping_type, self.price)

class Pizza(models.Model):
    pizza_type = models.ForeignKey(Pizza_Type, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)
    quantity = models.IntegerField()
    
class Order(models.Model):
    STATUS_OPTIONS = (('A', 'Active'),('S', 'Submitted'),('C', 'Complete'))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.ManyToManyField(Pizza, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    time = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
    

    