from store.models import Product 
class Cart():
    def __init__(self,request):
        self.session = request.session
        self.cart = self.session.get('cart', {})


    def add(self, product, quantity):
        product_id=str(product.id)
        product_qty = str(quantity)                  
        if product_id not in self.cart:
            self.cart[product_id] = product_qty
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
        self.cart[product_id]=product_qty
        self.session.modified=True
        return self.cart
    
    def remove(self, product):
        product_id=str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
            return self.cart
    
    def total(self):
        product=self.session['cart']
        total=0
        for id,quantity in product.items():
            total+= int(quantity)*int(Product.objects.get(id=id).price)
        return total



