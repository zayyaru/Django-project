from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='home_page'),
    path('about/', AboutPage, name='about_page'),
    path('service/', ServicePage, name='service_page'),
    path('contact/', ContactPage, name='contact_page'),
    

]