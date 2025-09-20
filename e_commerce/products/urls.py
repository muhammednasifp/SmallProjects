from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('list_product',views.list_product,name='list_product'),
    path('details_product/<pk>',views.details_product,name='details_product'),
]