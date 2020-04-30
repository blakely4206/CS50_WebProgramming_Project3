from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from orders.models import Customer, Pizza_Size, Pizza_Style, Pizza_Topping_Type, Topping, Pizza_Type, Pizza, Order, Pizza_Pic
from datetime import datetime, timedelta, time

ACTIVE = 'A'
COMPLETE = 'C'
SUBMITTED = 'S'

def index(request):
    return render(request, "main.html")
     
def menu(request): 
    if not request.user.is_authenticated:
        context = {
            "types": Pizza_Type.objects.all(),
            "toppings": Topping.objects.all(),
            "pics": Pizza_Pic.objects.all(),
            "logged_in": False
        }
       
        return render(request, "menu.html", context)
    
    else:
        current_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).exists()
    
        context = {
            "types": Pizza_Type.objects.all(),
            "sizes": Pizza_Size.objects.all(),
            "pics": Pizza_Pic.objects.all(),
            "styles": Pizza_Style.objects.all(),
            "topping_type": Pizza_Topping_Type.objects.all(),
            "toppings": Topping.objects.all(),
            "current_order": current_order,
            "logged_in": True
        }
       
        return render(request, "menu.html", context)    
        
def create_account(request):
    username = request.POST["username"]
    
    if User.objects.filter(username=username).exists():
        return render(request, "create_account.html", {"message": "Username exists"})
        
    else:
        password = request.POST["password1"]
        first = request.POST["first"]
        last = request.POST["last"]
        email = request.POST["username"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zip"]
        phone = request.POST["phone"]
        offers = request.POST.get("receive_emails")
           
        user = User.objects.create_user(username=username, email=username, password=password)
        user.save()    
        customer = Customer(user=user, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        customer.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
    
        return HttpResponseRedirect(reverse("create_order"))

def login_view(request):
    if 'create_account' in request.POST:
        return render(request, "create_account.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        
            return HttpResponseRedirect(reverse("create_order"))
        else:
            return render(request, "login.html", {"message": "Invalid credentials."})        

def create_order(request):
    if not request.user.is_authenticated:
    
        return render(request, "login.html", {"message": None})
    else:         
        order_pending = Order.objects.filter(user=request.user).filter(status=ACTIVE).exists()
        context = {
            "user": request.user,
            "address":request.user.customer.address,
            "city":request.user.customer.city,
            "state":request.user.customer.state,
            "zip_code":request.user.customer.zip_code,
            "first": request.user.first_name,
            "last": request.user.last_name,
            "sizes": Pizza_Size.objects.all(),
            "toppings" : Topping.objects.all(),
            "styles": Pizza_Style.objects.all(),
            "types": Pizza_Topping_Type.objects.all(),
            "order_pending": order_pending,
            "order": Order.objects.filter(user=request.user).filter(status=ACTIVE).first(),
            "logged_in": True
        }
        
        if request.method == 'POST':
            if 'Cancel' in request.POST:
                the_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
                the_order.delete()
                
                return render(request, "menu.html", context)
            elif 'Update' in request.POST:                
                current_items = request.POST.getlist('lineitems')
                quantity_items = request.POST.getlist('quantity')
                
                the_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
                               
                updated_order = Order(user=request.user, status='A')
                updated_order.save()
                
                for i in range(0, len(quantity_items)):  
                    pizza = the_order.contents.all()[i]
                    pizza.quantity = quantity_items[i]
                    pizza.save()
             
                the_order.total = total(Order.objects.filter(user=request.user).filter(status=ACTIVE).first().contents.all())
                the_order.save()
                
                return render(request, "cart.html", context)
            elif 'Order' in request.POST:
                the_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
                the_order.status = SUBMITTED
                the_order.save()
                
                return render(request, "confirmation.html", context)
            else:
                p_size = Pizza_Size.objects.get(size=request.POST.get("size"))
                p_style = Pizza_Style.objects.get(style=request.POST.get("style"))
                p_number_of_toppings = Pizza_Topping_Type.objects.get(value=request.POST.get("number_of_toppings"))
                p_toppings = request.POST.getlist('toppings')
                p_quantity = request.POST.get("quantity")
                p_type = get_object_or_404(Pizza_Type, size=p_size, style=p_style, topping_type=p_number_of_toppings)        
                p = Pizza(pizza_type=p_type, quantity=p_quantity)    
                p.save()
        
                for t in p_toppings:
                    topping = get_object_or_404(Topping, name=t)
                    p.toppings.add(topping)
            
                p_username = request.user
                customer = Customer.objects.get(user=p_username)
            
                the_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
            
                if the_order == None:
                    the_order = Order(user=request.user, status=ACTIVE, total=p_type.price)
                    the_order.save()
                    the_order.contents.add(p)
                    the_order.total = total(Order.objects.filter(user=request.user).filter(status=ACTIVE).first().contents.all())
                    the_order.save()                
                else:
                    the_order.contents.add(p)
                    the_order.total = total(Order.objects.filter(user=request.user).filter(status=ACTIVE).first().contents.all())
                    the_order.save()
                context['order'] = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
                
                return render(request, "cart.html", context)
        else:
            return render(request, "create_order.html", context)
        
def cart(request):
    context = {
        "order": Order.objects.filter(user=request.user).filter(status=ACTIVE).first(),
        "types": Pizza_Type.objects.all(),
        "toppings": Topping.objects.all(),
        "customer":request.user
    }
    
    if request.method == 'POST':
            if 'Cancel' in request.POST:
                the_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
                the_order.delete()
                context = {
                    "types": Pizza_Type.objects.all(),
                    "toppings": Topping.objects.all(),
                    "logged_in": True
                }
       
                return render(request, "menu.html", context)
            elif 'Update' in request.POST:                
                current_items = request.POST.getlist('lineitems')
                quantity_items = request.POST.getlist('quantity')
                
                the_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
                               
                updated_order = Order(user=request.user, status='A')
                updated_order.save()
                
                for i in range(0, len(quantity_items)):  
                    pizza = the_order.contents.all()[i]
                    pizza.quantity = quantity_items[i]
                    pizza.save()
             
                the_order.total = total(Order.objects.filter(user=request.user).filter(status=ACTIVE).first().contents.all())
                the_order.save()
                
                return render(request, "cart.html", context)
            elif 'Order' in request.POST:
                the_order = Order.objects.filter(user=request.user).filter(status=ACTIVE).first()
                the_order.status = SUBMITTED
                the_order.save()
                
                return render(request, "confirmation.html", context)
    else:
        return render(request, "cart.html", context)
  


def logout_view(request):
    context = {
        "pics": Pizza_Pic.objects.all(),
        "types": Pizza_Type.objects.all(),
        "toppings": Topping.objects.all(),
        "logged_in": False
    }
    logout(request)
    
    return render(request, "menu.html", context)
    
def total(the_order):
    the_total = 0
    
    for pizza in the_order:
        the_total += pizza.pizza_type.price * pizza.quantity
        
    return the_total