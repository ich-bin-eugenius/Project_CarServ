from django.urls import path
from .views import index


# ------------About------------

app_name = 'about'

urlpatterns = [
    path('', index, name='about'),
]


# ------------Contact------------

app_name = 'contact'

urlpatterns = [
    path('', index, name='contact'),
]


# ------------Home------------

app_name = 'home'

urlpatterns = [
    path('', index, name='home'),
]


# ------------Services------------

app_name = 'services'

urlpatterns = [
    path('', index, name='services'),
]
