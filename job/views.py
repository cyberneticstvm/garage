from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm, JobSparePartsForm
from .models import Job, Account, JobStatus, JobSparePart
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
            pickup_date = form.cleaned_data['pickup_date']
            job_description = form.cleaned_data['job_description']
            user = Account.objects.get(id=request.user.id)
            status = JobStatus.objects.get(id=1)
            staff = None
            Job.objects.create(job_id=job_id, brand_name=brand_name, model_name=model_name, make_year=make_year, color=color, pickup_required=pickup_required, pickup_address=pickup_address, pickup_date=pickup_date, job_description=job_description, user=user, status=status, staff=staff)
            messages.success(request, 'Service Request Submitted Successfully')
            return redirect('dashboard')
    else:
        form = JobForm()        
    context = {'form': form,}
    return render(request, 'customer/job.html', context)


@login_required(login_url = 'login')
def jobspareparts(request, id):
    job = get_object_or_404(Job, id=id)
    spareparts = JobSparePart.objects.filter(job_id=id)
    context = {'job' : job, 'spareparts' : spareparts}
    return render(request, 'staff/job-spare-parts.html', context)
        
    
@login_required(login_url = 'login')
def jobsparepartscreate(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == "POST":
        form = JobSparePartsForm(request.POST)
        if form.is_valid():
            spare_part_id = form.cleaned_data['spare_part_id']
            qty = form.cleaned_data['qty']
            cost_per_unit = form.cleaned_data['cost_per_unit']
            total = qty*cost_per_unit
            staff = get_object_or_404(Account, id=request.user.id)
            JobSparePart.objects.create(job_id=job, spare_part_id=spare_part_id, qty=qty, cost_per_unit=cost_per_unit, total=total, staff=staff)
            messages.success(request, 'Spare Part Updated Successfully')
            return redirect('jobspareparts', id)
    else:
        form = JobSparePartsForm()
        context = {'job' : job, 'form' : form}
        return render(request, 'staff/job-spare-parts-create.html', context)
    
@login_required(login_url = 'login')    
def jobsparepartsdelete(request, id):
    obj = get_object_or_404(JobSparePart, id=id)
    job = get_object_or_404(Job, job_id=obj.job_id)
    obj.delete()
    messages.success(request, "Spareparts Deleted Successfully")
    return redirect('jobspareparts', job.id)  