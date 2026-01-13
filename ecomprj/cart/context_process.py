from . import cart as c

def cart(request):
    return {'cart': c.Cart(request)}