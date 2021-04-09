from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from datetime import datetime, timedelta

def hello(request):
    return HttpResponse('<h1>HELLo</h1>')

def show_time(request):
    current_time = datetime.now() + timedalta(hours=int(hours))
    return HttpResponse(f'<h1>time: {current_time}</h1>')


product = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': i+1000,
    }
    for i in range(1, 10)
]

def products(request):
    return JsonResponse(product, safe=False)

def products_detail(request, products_id):
    for products in product:
        if products['id'] == products_id:
            return JsonResponse(products, status=200)
    return JsonResponse({'message': 'Product not found with selected to'}, status=100)