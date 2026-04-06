from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

def app(request):
    products = Product.objects.all()        
    return render(request, 'newApp/app.html', {'products': products})

def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    return render(request, 'newApp/contact.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'newApp/product_details.html', {'product': product})

def blog(request):
    return render(request, 'newApp/blog.html')

def faq(request):
    return render(request, 'newApp/faq.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('newApp:home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'newApp/login.html')
