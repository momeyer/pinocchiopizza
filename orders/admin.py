from django.contrib import admin
from .models import Pizza, Topping,OrderStatus, Sub, Extra, Pasta, Salad, DinnerPlate, Size, PizzaBaseType, PizzaTopping, Order, OrderItem

# Register your models here.


# Register your models here.
admin.site.register(PizzaTopping)
admin.site.register(PizzaBaseType)
admin.site.register(Size)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Extra)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlate)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(OrderStatus)

