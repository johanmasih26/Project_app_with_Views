

from django.urls import path, include
from .views import IndexView, ProductView, OrderCreateView, OrderUpdateView, OrderDeleteView
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('products/', ProductView.as_view(), name="products"),
    path('order-create/', OrderCreateView.as_view(), name="order_create"),
    path('order-update/<str:pk>', OrderUpdateView.as_view(), name="order_update"),
    path('order-delete/<str:pk>', OrderDeleteView.as_view(), name="order_delete"),
]
