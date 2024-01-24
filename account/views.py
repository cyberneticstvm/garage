from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):  
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = Account.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, phone_number = phone_number, password = password)
            user.is_active = True
            user.is_customer = True
            user.save()
            messages.success(request, 'Customer Registration Successful')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {'form': form,} 
    return render(request, 'register.html', context)
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            #messages.success(request, "You've logged in successfully")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url = 'login')    
def logout(request):
    auth.logout(request)
    messages.success(request, "You've logged out successfully")
    return redirect('login')