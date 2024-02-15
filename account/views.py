from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from job.models import Job
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

def edit(request):
    form = RegistrationForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'customer/profile-edit.html', context)

def update(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')           
    
    Account.objects.filter(id=request.user.id).update(first_name = first_name, last_name = last_name, email = email, phone_number = phone_number, username = username)       
    messages.success(request, "Customer Details Updated Successfully")
    return redirect('dashboard')
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_customer:
            auth.login(request, user)            
            messages.success(request, "You've logged in successfully")
            return redirect('dashboard')            
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    
    return render(request, 'login.html')

@login_required(login_url = 'login')
def dashboard(request):
    try:
        jobs = Job.objects.filter(user_id = request.user.id)
    except Job.DoesNotExist:
        jobs = None
    context = {'jobs': jobs,}
    return render(request, 'customer/dashboard.html', context)

@login_required(login_url = 'login')    
def logout(request):
    auth.logout(request)
    messages.success(request, "You've logged out successfully")
    return redirect('login')