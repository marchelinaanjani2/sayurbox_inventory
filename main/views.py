from ipaddress import summarize_address_range
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse




@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    if request.method == 'POST':
        if 'add_item' in request.POST:
            item_id = int(request.POST['add_item'])
            item = get_object_or_404(Item, id=item_id)
            item.amount += 1
            item.save()
        elif 'subtract_item' in request.POST:
            item_id = int(request.POST['subtract_item'])
            item = get_object_or_404(Item, id=item_id)
            if item.amount > 0:
                item.amount -= 1
                item.save()
        elif 'delete_item' in request.POST:
            item_id = int(request.POST['delete_item'])
            item = get_object_or_404(Item, id=item_id)
            item.delete()
    
    products = Item.objects.filter(user=request.user)
    total_stock = products.aggregate(total_stock=Sum('amount'))['total_stock'] or 0
    
    context = {
        'products': products,
        'nama': 'Marchelina Anjani S',
        'class': 'PBP B',
        'name': request.user.username,
        'total_stock': total_stock,
        # 'last_login': request.COOKIES['last_login'],
    }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)


# Fungsi untuk menambah amount suatu objek sebanyak satu
def add_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

# Fungsi untuk mengurangi jumlah stok suatu objek sebanyak satu
def subtract_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return redirect('main:show_main')

# Fungsi untuk menghapus suatu objek dari inventori
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('main:show_main')

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    # response.delete_cookie('last_login')
    return response

def get_product_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))


@csrf_exempt
def add_product_ajax(request):
    if  request.method == 'POST':
        name = request.POST.get("name")
        category = request.POST.get("category")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user 
        try:
            new_product = Item.objects.create(name=name, category=category, price=price, amount=amount, description=description, user=user)
            return JsonResponse({'success': True, 'message': 'Product added successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Error: ' + str(e)}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            category = data["category"],
            price = int(data["price"]),
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)