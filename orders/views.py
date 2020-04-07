from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from orders.models import Customer, Pizza_Size, Pizza_Style, Pizza_Topping_Type, Topping, Pizza_Type, Pizza, Order

def index(request):
    context = {
        "pizzas": Pizza_Type.objects.all(),
        "toppings" : Topping.objects.all()
    }
    return render(request, "menu.html", context)

def create_order(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    else:                
        context = {
            "user": request.user,
            "address":request.user.customer.address,
            "first": request.user.first_name,
            "last": request.user.last_name,
            "sizes": Pizza_Size.objects.all(),
            "toppings" : Topping.objects.all(),
            "styles": Pizza_Style.objects.all(),
            "types": Pizza_Topping_Type.objects.all(),
            "orders": Order.objects.filter(user=request.user)
        }
        
        if request.method == 'POST':
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
            
            return render(request, "cart.html", context)
        else:
            return render(request, "create_order.html", context)
        
def submit_order(request):
    context = {
        "pizzas": Pizza_Type.objects.all(),
        "orders": Order.objects.all(),
        "customer":request.user
    }
    
    
    return render(request, "menu.html", context)
    
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("create_order"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})