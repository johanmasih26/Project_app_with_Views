

from django.urls import path, include
from .views import IndexView, ProductView, OrderCreateView, OrderUpdateView, OrderDeleteView, LoginView, RegisterView
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('products/', ProductView.as_view(), name="products"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('order-create/', OrderCreateView.as_view(), name="order_create"),
    path('order-update/<str:pk>', OrderUpdateView.as_view(), name="order_update"),
    path('order-delete/<str:pk>', OrderDeleteView.as_view(), name="order_delete"),
]
