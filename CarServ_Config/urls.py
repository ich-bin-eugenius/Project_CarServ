"""
URL configuration for CarServ_Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, include
from apps.pages.views import index_404, index_500, index_team, index_testimonial
from apps.account.views import RegisterView, MyLoginView, user_logout
from apps.core.views import subscribe
from django.conf.urls.static import static
from CarServ_Config import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.core.urls')),

    path('404/', index_404, name='index_404'),
    path('500/', index_500, name='index_500'),
    path('team/', index_team, name='index_team'),
    path('testimonial/', index_testimonial, name='index_testimonial'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('subscribe/', subscribe, name='subscribe'),

    path('manager/', include('apps.manager.urls')),
]

handler404 = 'apps.pages.views.index_404'
handler500 = 'apps.pages.views.index_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
