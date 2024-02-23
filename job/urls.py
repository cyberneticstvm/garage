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
    path('create', views.create, name='create'),
    path('job-spare-parts/<id>', views.jobspareparts, name='jobspareparts'),
    path('job-spare-parts-create/<id>', views.jobsparepartscreate, name='jobsparepartscreate'),
    path('job-spare-parts-delete/<id>', views.jobsparepartsdelete, name='jobsparepartsdelete'),
    path('buy-customer-spare-part', views.buysparepart, name='buysparepart'),
    path('delete-customer-spare-part/<id>', views.customersparepartsdelete, name='customersparepartsdelete'),
    path('invoice/<id>', views.invoice, name='invoice'),
]
