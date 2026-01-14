from django.shortcuts import render,get_object_or_404
from .cart import Cart
from django.contrib import messages
from store.models import Product
from django.http import JsonResponse
from store.models import Product    


def cart_summary(request):
    cart=Cart(request)
    products_in_cart=cart.get_products()
    quantity=cart.get_quantity()
    return render(request,'cart_summary.html',{'products':products_in_cart, 'quantities':quantity,'total':cart.total()})


def cart_add(request):
    # to get the cart
    cart=Cart(request)
    # test for POST
    if request.POST.get('action')=='post':
        # to get the stuff
        product_id=int(request.POST.get('product_id'))
        # to search for the product in db
        product=get_object_or_404(Product,id=product_id)
        quantity=int(request.POST.get('product_qty'))
        #  save to seesion
        cart.add(product=product, quantity=quantity)
        #  get the cart quantity
        cart_quantity = cart.__len__()
        # return response
        # response=JsonResponse({'Product Name: ' : product.name})
        response = JsonResponse({'quantity': cart_quantity})
        
        messages.success(request,("You added this product to your cart!"))

        return response


def cart_remove(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        cart.remove(product=product_id)
        response = JsonResponse({'status':'Success'})
        messages.success(request,("You removed this product from your cart!"))
        return response

  
def cart_update(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request,("You updated this product quantity"))
        return response


    
