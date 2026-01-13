from store.models import Product 
class Cart():
    def __init__(self,request):
        self.session = request.session
        if('total' not in self.session):
            self.session['total']=0
        self.cart = self.session.get('cart', {})


    def add(self, product, quantity):
        product_id=str(product.id)
        product_qty = str(quantity)                  
        if product_id not in self.cart:
            self.cart[product_id] = product_qty
            self.session['total']+=int(product_qty)*int(product.price)
        self.session['cart'] = self.cart   
        self.session.modified = True
        return self.cart

    def __len__(self):
        return len(self.cart)
    

    def get_products(self):
        products_ids = self.cart.keys()
        product_in_cart = Product.objects.filter(id__in=products_ids)
        return product_in_cart
    

    def get_quantity(self):
        return self.cart
    

    def update(self, product, quantity):
        product_id=str(product)
        product_qty=str(quantity)
        self.session['total']+= (int(product_qty)-int(self.cart[product_id])) * int(Product.objects.get(id=product_id).price)
        self.cart[product_id]=product_qty
        self.session.modified=True
        return self.cart
    
    def remove(self, product):
        product_id=str(product)
        if product_id in self.cart:
            self.session['total']-=int(self.cart[product_id])*int(Product.objects.get(id=product_id).price)
            del self.cart[product_id]
            self.session.modified = True
            return self.cart
    
    def total(self):
        return self.session['total']

