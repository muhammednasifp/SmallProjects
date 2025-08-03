from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('list_product',views.list_product,name='list_product'),
    path('details_product',views.details_product,name='deatils_product'),
]