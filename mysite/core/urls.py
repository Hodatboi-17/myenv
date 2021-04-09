from django.urls import path
from core.views import products,products_detail

urlpatterns = [
    path('product/', products),
    path('product/<int:products_id>/', products_detail)
]