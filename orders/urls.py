from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("menu/<str:category>", views.menu, name="menu"),
    path("add/<str:category>/<str:name>/<str:price>", views.add, name="add"),
    path("my_orders/<str:order_number>", views.my_orders, name="my_orders"),
    path("orders_manager/<str:user>/<str:order_number>", views.orders_manager, name="orders_manager"),
    path("complete_order/<str:user>/<str:order_number>", views.complete_order, name="complete_order"),
    path("confirmed/<str:order_number>", views.confirmed, name="confirmed"),
    path("delete/<str:category>/<str:name>/<str:price>", views.delete, name="delete"),
]
