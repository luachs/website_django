import json
from django.http import HttpResponse, JsonResponse # type: ignore
from django.template import loader # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.contrib import messages # type: ignore
from .models import *
from django.contrib.auth.forms import UserCreationForm # type: ignore

# Create your views here.
def detail(request):
  if request.user.is_authenticated:
     customer = request.user
     order, created = Order.objects.get_or_create(customer = customer, complete = False) 
     items = order.orderitem_set.all()
     cartItems = order.get_cart_items
     user_login = "show"
     user_not_login = "hidden"
  else:
     items = []
     order = {'get_cart_items' : 0 , 'get_cart_total':0}
     cartItems = order['get_cart_items']
     user_login = "hidden"
     user_not_login = "show"
  id =request.GET.get('id','')
  products =Product.objects.filter(id = id)
  context = {'items' :items, 
             "order" : order, 
             'user_login': user_login,
             'user_not_login':user_not_login,
             'cartItems':cartItems,
              'products':products
             }
  return render(request, 'detail.html', context)

def category(request):
    categories = Category.objects.filter(is_sub =False)
    active_category = request.GET.get('category','')
    if request.user.is_authenticated:
       customer = request.user
       order, created = Order.objects.get_or_create(customer=customer, complete=False)
       cartItems = order.get_cart_items
       user_login = "show"
       user_not_login = "hidden"
    else:
       order = {'get_cart_items' : 0 , 'get_cart_total':0}
       cartItems = order['get_cart_items']
       user_login = "hidden"
       user_not_login = "show"
    products = Product.objects.all()
  
    if active_category:
        products=Product.objects.filter(category__slug = active_category)
    context = {
        'categories':categories,
        'active_category':active_category,
        'products': products,
        'user_authenticated': request.user.is_authenticated,
        'user_username': request.user.username,
        'cartItems':cartItems,
        'user_login': user_login,
        'user_not_login':user_not_login
    }
    return render(request, 'category.html', context)
def search(request):
   if request.method == 'POST':
      searched =request.POST['searched']
      keys = Product.objects.filter(name__contains =searched)
   if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_login = "show"
        user_not_login = "hidden"
   else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_login = "hidden"
        user_not_login = "show"
   context = {
       'items' :items, "order" : order,
       'searched':searched ,
       'keys':keys,
       'cartItems':cartItems,
       'user_login': user_login,
       'user_not_login':user_not_login,
        }
   return render(request, 'search.html', context)

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_login = "show"
        user_not_login = "hidden"
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        user_login = "hidden"
        user_not_login = "show"
    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems,
        'user_authenticated': request.user.is_authenticated,
        'user_username': request.user.username,
        'user_login': user_login,
        'user_not_login':user_not_login
    }
    return render(request, 'index.html', context)

def show_products(request):
    categories = Category.objects.filter(is_sub =False)
    active_category = request.GET.get('category','')
    if request.user.is_authenticated:
       customer = request.user
       order, created = Order.objects.get_or_create(customer=customer, complete=False)
       cartItems = order.get_cart_items
       user_login = "show"
       user_not_login = "hidden"
    else:
       order = {'get_cart_items' : 0 , 'get_cart_total':0}
       cartItems = order['get_cart_items']
       user_login = "hidden"
       user_not_login = "show"
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products': products,
        'user_authenticated': request.user.is_authenticated,
        'user_username': request.user.username,
        'cartItems':cartItems,
        'user_login': user_login,
        'user_not_login':user_not_login
    }
    return render(request, 'show_product.html', context)
def cart(request):
  if request.user.is_authenticated:
     customer = request.user
     order, created = Order.objects.get_or_create(customer = customer, complete = False) 
     items = order.orderitem_set.all()
     cartItems = order.get_cart_items
     user_login = "show"
     user_not_login = "hidden"
  else:
     items = []
     order = {'get_cart_items' : 0 , 'get_cart_total':0}
     cartItems = order['get_cart_items']
     user_login = "hidden"
     user_not_login = "show"
  context = {'items' :items, 
             "order" : order, 
             'user_login': user_login,
             'user_not_login':user_not_login,
             'cartItems':cartItems,
             }
  return render(request, 'cart.html', context)

def contact(request):
    if request.user.is_authenticated:
       customer = request.user
       order, created = Order.objects.get_or_create(customer=customer, complete=False)
       cartItems = order.get_cart_items
       user_login = "show"
       user_not_login = "hidden"
    else:
       order = {'get_cart_items' : 0 , 'get_cart_total':0}
       cartItems = order['get_cart_items']
       user_login = "hidden"
       user_not_login = "show"
    context = {
             "order" : order, 
             'user_login': user_login,
             'user_not_login':user_not_login,
             'cartItems':cartItems,
             }
    return render(request, 'contact.html', context)
def payment(request):
    if request.user.is_authenticated:
       customer = request.user
       order, created = Order.objects.get_or_create(customer=customer, complete=False)
       cartItems = order.get_cart_items
       user_login = "show"
       user_not_login = "hidden"
    else:
       cartItems = order['get_cart_items']
       user_login = "hidden"
       user_not_login = "show"
    context = {
             "order" : order, 
             'user_login': user_login,
             'user_not_login':user_not_login,
             'cartItems':cartItems,
             }
    template = loader.get_template('payment.html')
    return HttpResponse(template.render(context))
def updateItem(request):
   
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse({'message': 'Item updated successfully'}, safe=False)
  




# login
def loginPage(request):
    if request.user.is_authenticated:
       user_login = "show"
       user_not_login = "hidden"
       return redirect('home')
    else:
       user_login = "hidden"
       user_not_login = "show"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    form = UserCreationForm() 
    context ={'form': form, 'user_login': user_login,'user_not_login':user_not_login}
    return render(request, 'login.html', context)

def register(request):
    if request.user.is_authenticated:
       user_login = "show"
       user_not_login = "hidden"
    else:
       user_login = "hidden"
       user_not_login = "show"
    form = CreateUserForm() 
    if request.method == 'POST':
       form = CreateUserForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request, 'Account created successfully. Please log in.')
          return redirect('login')
       else:
          messages.error(request, 'There was an error with your submission.')
    context ={'form': form, 'user_login': user_login,'user_not_login':user_not_login}
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']
    #     if password == password2:
    #         if User.objects.filter(username=username).exists():
    #             messages.error(request, 'Username already exists.')
    #         else:
    #             User.objects.create_user(username=username, password=password)
    #             messages.success(request, 'Account created successfully.')
    #             return redirect('login')
    #     else:
    #         messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')





