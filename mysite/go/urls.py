from django.urls import path,re_path
from go.views import hello, show_time,products,products_detail

urlpatterns = [
    path('hi/', hello),
    re_path('time/plus/(\d{1,2})/', show_time),
    path('products/', products),
    path('products/<int:products_id>/', products_detail)
]
