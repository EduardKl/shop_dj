from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *
from cart.forms import CartAddProductForm

# Create your views here.
def pageNotFound(request, exception):
    return HttpResponse('404')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/products_list.html', {'title': 'Список товаров',
                                'category': category,
                                'categories': categories,
                                'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'shop/product_detail.html',
                  {'title': product.name,
                   'product': product,
                   'cart_product_form': CartAddProductForm()})