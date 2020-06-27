from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("pizza/", views.orderPizza, name="orderPizza"),
    path("Sub/", views.orderSub, name="orderSub"),
    path("Pasta/", views.orderPasta, name="orderPasta"),
    path("Dinner/", views.orderDinner, name="orderDinner"),
    path("Salad/", views.orderSalad, name="orderSalad"),
    path("register/", views.register, name="register"),
    path("Remove/", views.removeItem, name="removeItem"),
    path("Checkout/", views.checkout, name="checkout")
]

