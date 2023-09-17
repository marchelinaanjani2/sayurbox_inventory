from django.forms import ModelForm
from main.item import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "price", "amount", "description"]