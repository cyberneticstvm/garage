"""
URL configuration for workshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('edit', views.edit, name='edit'),
    path('update', views.update, name='update'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('editjobstatus/<id>', views.editjobstatus, name='editjobstatus'),
    path('staffdashboard', views.staffdashboard, name='staffdashboard'),
    path('changepassword', views.changePassword, name='changepwd'),
    path('logout', views.logout, name='logout'),
]
