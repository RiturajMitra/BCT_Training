from .models import Product
from django.shortcuts import render

def app(request):
    products = Product.objects.all()
    return render(request,'newApp/app.html' , {'products': products})
def app(request):
    return render(request, 'newApp/app.html')
def about(request):
    return render(request, 'newApp/about.html')
def contacts(request):
    return render(request, 'newApp/contacts.html')      