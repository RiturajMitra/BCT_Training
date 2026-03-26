from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")
def about(request):
    return HttpResponse("About")
def contacts(request):
    return HttpResponse("Contacts")
def services(request):
    return HttpResponse("Services")