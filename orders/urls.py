from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("create_order", views.create_order, name="create_order"),
    path("create_account", views.create_account, name="create_account"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("cart", views.cart, name="cart")
]
