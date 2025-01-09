from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('product/', views.show_products, name='product'),  # Sản phẩm
    path('cart/', views.cart, name='cart'),  # Giỏ hàng
    path('contact/', views.contact, name='contact'),  # Liên hệ
    path('payment/', views.payment, name='payment'),  # Liên hệ
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
