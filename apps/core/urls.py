from django.urls import path
from .views import index_home, index_about, index_services, index_contact

app_name = 'home'

urlpatterns = [
    path('', index_home, name='home'),
    path('about/', index_about, name='about'),
    path('services/', index_services, name='services'),
    path('contact/', index_contact, name='contact'),
]