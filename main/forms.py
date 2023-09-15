from django.forms import ModelForm
from main.item import Product

class ProductForm(ModelForm):
    class Meta:
        item = Product
        fields = ["name", "category", "price", "amount", "description"]