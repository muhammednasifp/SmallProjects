from django.urls import path
from . import views
urlpatterns = [
   
    path('account_details',views.account_details,name='account'),

]