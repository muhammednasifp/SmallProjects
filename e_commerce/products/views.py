from django.shortcuts import render
from . models import Product
# Create your views here.

def index(request):
    return render(request,'index.html')

def list_product(request):
    product_list=Product.objects.all()
    
    return render(request,'products.html',{'products':product_list})

def details_product(request):
    return render(request,'product_details.html')
