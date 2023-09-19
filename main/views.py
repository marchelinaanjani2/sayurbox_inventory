from ipaddress import summarize_address_range
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.item import Product
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    total_stock = products.aggregate(total_stock=Sum('amount'))['total_stock'] or 0
    context = {
        'products': products,
        'total_stock': total_stock, 
     }
        
    return render(request, "main.html", context)


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.stock = product.amount  # Set stok awal sama dengan jumlah produk yang ditambahkan
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
