from django.forms import ModelForm
from main.item import Product
from django import forms
from django.db import models


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "price", "stock", "description"]