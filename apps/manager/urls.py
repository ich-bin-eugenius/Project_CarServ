from django.urls import path
from .views import index

app_name = 'manager'

urlpatterns = [
    path('', index, name='manager'),
]
