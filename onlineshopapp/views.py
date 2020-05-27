from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import HttpResponseRedirect, reverse

from .models import Product

def count_total_items(request):
    total_items = 0
    if 'cart' in request.session:
        total_items = len(request.session['cart'])
    return total_items

# Create your views here.
class HomeView(ListView):
    template_name= 'home.html'
    model = Product
    
    # menambahkan context dalam ListView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = count_total_items(self.request)

        return context
    

class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        if 'counter_session' in request.session:
            counter = request.session['counter_session']

        return render(request, self.template_name, {'counter':counter})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = count_total_items(self.request) 
        return context
    


class AddedToCartView(TemplateView):
    template_name="cart/added.html"
    id = None

    def get(self, request, id):
        cart_products = None
        if "cart" in request.session:
            cart_products = request.session['cart']
            # [{'id':1, 'quantity':2}, {'id':3, 'quantity':5}]
            cart_products.append({'id':id, 'quantity':1})
            
            # simpan ke dalam session yang sama
            request.session['cart'] = cart_products
        else:
            request.session['cart'] = []
            cart_products = request.session['cart']
            cart_products.append({'id':id, 'quantity':1})
            request.session['cart'] = cart_products
            
        return render(request, self.template_name, {'product':len(cart_products)})


class ShoppingCartView(TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request):
        
        products = []
        if 'cart' in request.session:
            print(request.session['cart'])
            items_in_cart = request.session['cart']
            for item in items_in_cart:
                products.append(Product.objects.get(id=item['id']))
        
        return render(request, self.template_name, {'products_in_cart':products, 'cart':count_total_items(request)})       
