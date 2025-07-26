from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrdersForm
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .forms import *


def set_up_cloud(file, instance):
    file_path = default_storage.save(file, ContentFile(file.read()))
    instance.photo = file_path
    instance.save()


def index(request):
    pro = Product.objects.all()
    cus = Customer.objects.all()
    ord = Orders.objects.all()
    context = {
        "pro": pro,
        "cus": cus,
        "ord": ord
    }
    return render(request, "index.html", context=context)

def product(request, pk):
    pro = Product.objects.all()
    cus = Customer.objects.all()
    ord = Orders.objects.filter(product_id=pk)
    context = {
        "pro": pro,
        "cus": cus,
        "ord": ord
    }
    return render(request, "product.html", context=context)

def product_wiev(request):
    pro = Product.objects.all()

    return render(request, 'product.html', {"product" : pro})

def customer(request, pk):
    pro = Product.objects.all()
    cus = Customer.objects.all()
    ord = Orders.objects.filter(customer_id=pk)
    context = {
        "pro": pro,
        "cus": cus,
        "ord": ord
    }
    return render(request, "customer.html", context=context)

def cust_wiev(request):
    cus = Customer.objects.all()

    return render(request, 'customer.html', {"customers" : cus})


def orders(request, pk):
    try:
        ord = Orders.objects.get(pk=pk)
        pro = Product.objects.filter(id=ord.product_id.id)
        cus = Customer.objects.filter(id=ord.customer_id.id)
    except Orders.DoesNotExist:
        ord = None
        pro = []
        cus = []
        context = {
            "pro": pro,
            "cus": cus,
            "ord": ord
        }
        return render(request, "orders.html", context=context)

def add_product(request):
    if request.method == 'POST':
        print("==============", request.POST)
        form = OrdersForm(request.POST)
        if form.is_valid():
            print("==========", form.cleaned_data)
            pro = Product.objects.create(**form.cleaned_data)
            return redirect('index')

    else:
        form = OrdersForm()
    return render(request, 'add_product.html', context={'form': form})

def add_customer(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            print("==========", form.cleaned_data)
            cus = Customer.objects.create(**form.cleaned_data)
            return redirect('index')

    else:
        form = OrdersForm()
    return render(request, 'add_customer.html', context={'form': form})
