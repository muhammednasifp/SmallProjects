from django.db import models
from customers.models import Customers
from products.models import Product

# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),
                    (DELETE,'delete'))
    
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=-1
    STATUS_CHOICES=((ORDER_CONFIRMED,'order_confirmed'),
                    (ORDER_PROCESSED,'order_processed'),
                    (ORDER_REJECTED,'order_rejected'))

    owner=models.ForeignKey(Customers,
                            on_delete=models.SET_NULL,
                            null=True,
                            related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES,
                                        default=LIVE)
    order_status=models.IntegerField(choices=STATUS_CHOICES,
                                     default=CART_STAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    product=models.ForeignKey(Product,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='added_cart')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='aded_items')
    

    