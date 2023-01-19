from django.shortcuts import render
from .models import Product
# Create your views here.

def get_product(request,product_id):
    product = Product.objects.get(id=product_id)

    return render (request,"product_detail.html", context=product)



def get_products (request):
    products = Product.object.all()
    context = {"Products" : products}
    return render (request, "product_list.html",context)


