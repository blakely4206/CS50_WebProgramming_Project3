from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from orders.models import Customer
from orders.models import Pizza
from orders.models import Pizza_Topping_Type
from orders.models import Pizza_Size
from orders.models import Topping
from orders.models import Pizza_Type
from orders.models import Order
from orders.models import Pizza_Style
from orders.models import Pizza_Pic

admin.site.register(Customer)
admin.site.register(Pizza_Size)
admin.site.register(Pizza_Topping_Type)
admin.site.register(Topping)
admin.site.register(Pizza_Type)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Pizza_Style)
admin.site.register(Pizza_Pic)