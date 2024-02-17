from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm, JobSparePartsForm
from .models import Job, Account, JobStatus, JobSparePart
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import date
from django.db.models import Sum

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

@login_required(login_url = 'login')    
def invoice(request, id):
    job = get_object_or_404(Job, id=id)
    customer = get_object_or_404(Account, id=job.user.id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    spares = JobSparePart.objects.filter(job_id=job.id).all()
    
    x_start = 200
    y_start = 750
    
    p = canvas.Canvas(response)
    
    img_file = 'http://localhost:8000/static/admin/assets/images/logo-png.png'
    
    p.drawString(220, 770, "Super Car Garage")
    p.drawString(240, 750, "Trivandrum")
    p.drawString(200, 730, "Phone: +91 0123456789")
    
    p.drawString(50, 710, "-------------------------------------------------------------------------------------------------------------------------" )
    
    p.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
    p.drawString(50, 690, "Customer Name:" + customer.first_name +" "+ customer.last_name)
    p.drawString(400, 690, "Job ID:" + job.job_id)
    p.drawString(50, 670, "Invoice No:" + str(job.id))
    p.drawString(400, 670, "Invoice Date:"+ str(date.today().strftime("%B %d, %Y")) )
    
    p.drawString(240, 650, "INVOICE" )
    
    row_height = 20
    column_width = 150
    tot = 0
    
    data = [
        ['SPARE NAME', 'QTY', 'COST', 'TOTAL'],
    ]
    tot = 0
    for obj in spares:
        data.append([obj.spare_part_id, obj.qty, obj.cost_per_unit, obj.total])
        tot += float(obj.total)
        
    x = 50
    y = 610
    for row in data:
        for item in row:
            p.drawString(x, y, str(item))
            x += column_width
        x = 50
        y -= row_height
    
    y += -10
    
    p.drawString(50, y, "-------------------------------------------------------------------------------------------------------------------------" )
    y += -15    
    p.drawString(50, y, '' )
    p.drawString(200, y, '' )
    p.drawString(350, y, 'Total' )
    p.drawString(500, y, str(tot)+'0')
    
    p.showPage()
    p.save()
    return response