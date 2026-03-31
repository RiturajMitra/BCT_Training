from django.shortcuts import render

def app(request):
    return render(request, 'newApp/app.html')
def about(request):
    return render(request, 'newApp/about.html')
def contacts(request):
    return render(request, 'newApp/contacts.html')      
# Create your views here.

