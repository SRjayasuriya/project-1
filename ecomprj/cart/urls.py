from django.urls import path
from . import  views

urlpatterns= [
    path('',views.cart_summary,name='cart-summary'),
    path('add/', views.cart_add,name='cart-add'),
    path('remove/',views.cart_remove,name='cart-remove'),
    path('update/', views.cart_update,name='cart-update'),
]