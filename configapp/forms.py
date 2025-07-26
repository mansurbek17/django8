from django.core.exceptions import ValidationError
from django import forms
from .models import *


class OrdersForm(forms.Form):
    # class Meta:
    #     model = Orders
    #     fields = ['product_id', 'customer_id', 'quantity', 'required_date']
    product_id = forms.ModelChoiceField(empty_label="Pruducts",
                                        label="Products", queryset=Product.objects.all(),
                                        widget=forms.Select(attrs={"class": "form-control"}))

    customer_id = forms.ModelChoiceField(empty_label="Customers",
                                         label="Customers", queryset=Customer.objects.all(),
                                         widget=forms.Select(attrs={"class": "form-control"}))

    quantity = forms.IntegerField(min_value=1, label="Quantity",
                                  widget=forms.NumberInput(attrs={"class": "form-control"}))