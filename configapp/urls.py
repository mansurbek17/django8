from django.urls import path
from configapp.views import *

urlpatterns = [
    path('', index, name="home"),
    path("add_product/", add_product, name="add_product"),
    path("add_customer/", add_customer, name="add_customer"),
    path("customer/<int:pk>/", customer, name="customer"),
    path("prodcut/<int:pk>/", product, name="product"),
    path("orders/<int:pk>/", orders, name="orders"),
    path("prodcut/", product_wiev, name="product_wiev"),
    path("customer1/", cust_wiev, name="customer_wiev"),
    ]

