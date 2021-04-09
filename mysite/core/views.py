from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

def products(request):
    return JsonResponse(products, safe=False)

def products_detail(request, product_id):
    for products in product:
        if products['id'] == products_id:
            return JsonResponse(products, status=200)
    return JsonResponse({'messgge': 'Product not found with selected to'}, status=100)


