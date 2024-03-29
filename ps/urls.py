"""ps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App.business import views

from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path('administracion/de/recursos/de/about/y/project', admin.site.urls),
    path('', include('App.ps.urls')),
    path('business/', include('App.business.urls')),
    path('zetone/', include('App.zetone.urls')),
    path('vikosur/', include('App.vikosur.urls')),
    
    path('accounts/login/', LoginView.as_view(template_name='business/registration/login.html'), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('accounts/profile/', views.business, name="business"),
]
