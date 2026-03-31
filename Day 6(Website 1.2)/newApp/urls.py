from django.urls import path
from . import views

urlpatterns = [
    path('',views.app,name='app'),
    path('about/',views.about,name='about'),
    path('contacts/',views.contacts,name='contacts'),
   
]