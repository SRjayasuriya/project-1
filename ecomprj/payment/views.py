from django.shortcuts import render,redirect
from django.http import HttpResponse
from cart.cart import Cart
from .form import ShippingForm, PaymentForm
from .models import ShippingAddress,Order,OrderItem
from django.contrib import messages
from store.models import Product

# Create your views here.

def process_payement(request):
    if request.POST:
        shipping = request.session.get('billing_info')
        name= shipping['delivery_full_name']
        email = shipping['delivery_email']
        address= shipping['delivery_address_line1'] + " " + shipping['delivery_address_line2']
        cart=Cart(request)
        amount = cart.total()
        order = Order.objects.create(user=request.user, full_name=name, email=email, shipping_address=address, amount_paid=amount)
        order.save()
        order_id = Order.objects.get(id=order.id)
        for id,quantity in cart.get_quantity().items():
            product=Product.objects.get(id=id)
            order_item = OrderItem.objects.create(user=request.user, order=order_id, product_id=id, quantity=quantity, price=product.price)
            order_item.save()
        request.session['cart']={}
        messages.success(request,"Payment successful!")
        return redirect('home')
    else:
        messages.success(request,"Access denied!")
        return redirect('home')
        
def payment_success(request):
    return render(request, 'payment_success.html',)

def checkout(request):   
    if request.user.is_authenticated:
        prod= Cart(request).get_quantity()
        products = []
        for id, quantity in prod.items():
            product = Cart(request).get_products().get(id=id)
            products.append((product.name,product.price,quantity, int(product.price) * int(quantity))) 
        shipping_user = ShippingAddress.objects.get(user_id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if request.method == 'POST':
            if shipping_form.is_valid():
                return redirect('billing_info')
            else:
                messages.success(request,"Fill the form correctly")
                return redirect('checkout')
        else:
            return render(request, 'checkout.html', {'products': products, 'overall':Cart(request).total(), 'form':shipping_form})
    else:
        messages.success(request,"Please log in!")
        return redirect('login')
def billing_info(request):
    if request.POST:   
        prod= Cart(request).get_quantity()
        products = []
        for id, quantity in prod.items():
            product = Cart(request).get_products().get(id=id)
            products.append((product.name,product.price,quantity, int(product.price) * int(quantity)))    
        Billing_form = PaymentForm()
        shipping_user = ShippingAddress.objects.get(user_id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        request.session['billing_info'] = request.POST
        return render(request, 'billing_info.html', {'products': products, 'overall':Cart(request).total(), 'shipping_form':shipping_form,'billing_form':Billing_form})
    else:
        messages.success(request,"Access denied!")
        return redirect('home')