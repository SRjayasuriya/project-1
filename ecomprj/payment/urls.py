from django.urls import path
from . import views

urlpatterns = [
    path('payment_success/',views.payment_success,name='payment_success'),
    path('checkout/',views.checkout,name='checkout'),
    path('billing_info/',views.billing_info,name='billing_info'),
    path('process_payment/',views.process_payement,name='process_payment'),
    path('shipped_orders/',views.shipped_orders,name='shipped_orders'),
    path('unshipped_orders/',views.unshipped_orders,name='unshipped_orders'),
    path('order_details/<int:order_id>/',views.order_details,name='order_details'),
    path('mark_shipped/<int:order_id>/',views.mark_shipped,name='mark_shipped'),
    path('mark_unshipped/<int:order_id>/',views.mark_unshipped,name='mark_unshipped'),
    path('delete_order/<int:order_id>/',views.delete_order,name='delete_order'),
]