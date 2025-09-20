from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
#paginator is used to make different pages in the webpage
# Create your views here.

def home(request):
    featured_pList=Product.objects.order_by('-priority')[:4]
    latest_pList=Product.objects.order_by('priority')[:4]
    context={'featured_List':featured_pList,
             'latest_list':latest_pList
            }
    return render(request,'index.html',context)
    

def list_product(request):      
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    #product_list=Product.objects.all()
    product_list=Product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,2)
    #here paginator constructor created with two items
    product_list=product_paginator.get_page(page)
    return render(request,'products.html',{'products':product_list})

def details_product(request,pk):
    product_details=Product.objects.get(pk=pk)
    context={'pDetails':product_details}
    return render(request,'product_details.html',context)
