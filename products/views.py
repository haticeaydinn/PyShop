from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# index means main home page
def index(request):
    return HttpResponse('Welcome to Products Page')


def new(request):
    return HttpResponse('New Products')
