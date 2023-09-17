from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.item import Product
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        'name': 'Mangga Harum Manis',
        'category': 'Buah-buahan',
        'price': '19.900',
        'amount': '30',
        'description': '''Tersedia dalam pilihan konvensional dan imperfect. Mangga imperfect memiliki bercak pada kulitnya, ukuran yang lebih kecil dan tekstur lembek di beberapa bagian sehingga disarankan agar dapat langsung dikonsumsi. Sementara Mangga konvensional perlu ditunggu 2-3 hari agar matang sempurna.

                            Mangga harum manis memiliki kulit yang mulus, rasanya manis, wanginya khas, dan tekstur juicy. Cocok dibuat jus, dimakan sebagai camilan sehat, dibuat selai, atau kreasi lainnya.

                            Terdapat potensi kelebihan/kekurangan gramasi +-10% per pack.''',
        'products': products

                                }
        

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

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

# ##bonus
# def jumlah_item(request):
#     products = Product.objects.all()  # Mengambil semua produk
#     num_products = products.count()    # Menghitung jumlah produk

#     context = {
#         'products': products,
#         'num_products': num_products,  # Mengirimkan jumlah produk ke template
#     }

#     return render(request, 'main.html', context)