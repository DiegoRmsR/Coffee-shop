from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPI

urlpatterns = [
    path('api/', ProductListAPI.as_view(), name="product_list_api"),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('add/', ProductFormView.as_view(), name="add_product"),
]
