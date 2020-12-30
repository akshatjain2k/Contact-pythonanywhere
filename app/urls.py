from django.urls import path
from app import views

urlpatterns = [
    path('contact', views.contact, name="contact")
]