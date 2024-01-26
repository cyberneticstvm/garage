from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job, Account, JobStatus
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random

# Create your views here.

@login_required(login_url = 'login')
def create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job_id = 'JOB-'+ str(random.randrange(10000, 99999))
            brand_name = form.cleaned_data['brand_name']
            model_name = form.cleaned_data['model_name']
            make_year = form.cleaned_data['make_year']
            color = form.cleaned_data['color']
            pickup_required = form.cleaned_data['pickup_required']
            pickup_address = form.cleaned_data['pickup_address']
            job_description = form.cleaned_data['job_description']
            user = Account.objects.get(id=request.user.id)
            status = JobStatus.objects.get(id=1)
            staff = None
            Job.objects.create(job_id=job_id, brand_name=brand_name, model_name=model_name, make_year=make_year, color=color, pickup_required=pickup_required, pickup_address=pickup_address, job_description=job_description, user=user, status=status, staff=staff)
            messages.success(request, 'Service Request Submitted Successfully')
            return redirect('dashboard')
    else:
        form = JobForm()        
    context = {'form': form,}
    return render(request, 'customer/job.html', context)
