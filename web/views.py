from django.shortcuts import render, redirect
from .models import Callback
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        service = request.POST['service']
        Callback.objects.create(name=name, mobile=mobile, service=service)
        messages.success(request, 'Service Request Submitted Successfully')
        return redirect('index')
    return render(request, 'index.html')