from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
# index means main home page
def index(request):
    products = Product.objects.all()  # to get all products in table
    # Product.object.filter() to filter ex. cheaper than 2 dollars
    # Product.object.get() to get one product
    # Product.object.save()
    # return HttpResponse('Welcome to Products Page')
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('New Products')
