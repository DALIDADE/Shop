from django.urls import path
from .views import *
urlpatterns = [
    path('',Store,name='store'),
    path('checkout/',Checkout,name='checkout'),
    path('cart/',Cart,name='cart'),
    path('update_item/',updateItm,name = 'update_item ')
]
