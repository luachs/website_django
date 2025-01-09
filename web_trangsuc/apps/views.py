from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.contrib import messages # type: ignore
from .models import *
from django.contrib.auth.decorators import login_required # type: ignore


# Create your views here.

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
@login_required
def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'user_authenticated': request.user.is_authenticated,
        'user_username': request.user.username,
    }
    return render(request, 'show_product.html', context)
def cart(request):
  if request.user.is_authenticated:
     customer = request.user
     order, created = Order.objects.get_or_create(customer = customer, complete = False) 
     items = order.orderitem_set.all()
  else:
     items = []
     order = {'get_cart_items' : 0 , 'get_cart_total':0}
  context = {'items' :items, "order" : order}
  template = loader.get_template('cart.html')
  return HttpResponse(template.render(context))

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())
def payment(request):
  template = loader.get_template('payment.html')
  return HttpResponse(template.render())

# login
























def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')