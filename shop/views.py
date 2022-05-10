from doctest import debug
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
# Create your views here.
def index(request):

    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("we are at about")

def contact(request):
    return HttpResponse("we are at contact")

def productView(request):
    return HttpResponse("we are at prod view")

def track(request):
    return HttpResponse("we are at tracker")
    
def search(request):
    return HttpResponse("we are at search")

def checkout(request):
    return HttpResponse("we are at checkout")

