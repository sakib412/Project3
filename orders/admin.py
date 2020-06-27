from django.contrib import admin
from .models import Category,RegularPizza,SicilianPizza,Topping,Sub,Pasta,Salad,DinnerPlatter,Order,UserOrder,OrderCounter

# Register your models here.
admin.site.register(Category)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Order)
admin.site.register(UserOrder)
admin.site.register(OrderCounter)