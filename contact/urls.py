from django.contrib import admin
from django.urls import path, include
from .views import index, contact_view, contact_page

urlpatterns = [
    path('', index, name='index'), 
    path('contact/', contact_page, name='contact_page'),  # Frontend page
    path('api/contact/', contact_view, name='contact_api'), 
    
    ]