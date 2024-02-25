from django.shortcuts import render, redirect, get_object_or_404
from .forms import SparepartsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Spareparts
# Create your views here.


@login_required(login_url = 'login')
def create(request):
    if request.method == 'POST':
        form = SparepartsForm(request.POST)
        if form.is_valid():
            spare_part_name = form.cleaned_data['spare_part_name']
            cost_per_unit = form.cleaned_data['cost_per_unit']
            Spareparts.objects.create(spare_part_name=spare_part_name, cost_per_unit=cost_per_unit)
            messages.success(request, 'Sparepart Created Successfully')
            return redirect('createsp')
    else:
        form = SparepartsForm()
    context = {'form': form,}
    if request.user.is_admin and request.user.is_superadmin:
        return render(request, 'administrator/sparepart-create.html', context)
    else:
        return render(request, 'staff/sparepart-create.html', context)

@login_required(login_url = 'login')
def list(request):
    try:
        spareparts = Spareparts.objects.all()
    except spareparts.DoesNotExist:
        spareparts = None
    context = {'spareparts': spareparts,}
    if request.user.is_admin and request.user.is_superadmin:
        return render(request, 'administrator/spareparts-list.html', context)
    else:
        return render(request, 'staff/spareparts-list.html', context)

@login_required(login_url = 'login')
def edit(request, id):    
    if request.method == 'POST':
        spare_part_name = request.POST.get('spare_part_name')
        cost_per_unit = request.POST.get('cost_per_unit')
        Spareparts.objects.filter(id=id).update(spare_part_name=spare_part_name, cost_per_unit=cost_per_unit)
        messages.success(request, "Spareparts Updated Successfully")
        return redirect('listsp')
    else:
        form = SparepartsForm(instance = get_object_or_404(Spareparts, id=id))
        context = {'form': form, 'id': id}
        if request.user.is_admin and request.user.is_superadmin:
            return render(request, 'administrator/sparepart-edit.html', context)
        else:
            return render(request, 'staff/sparepart-edit.html', context)
    
@login_required(login_url = 'login')
def delete(request, id):
    obj = get_object_or_404(Spareparts, id=id)
    obj.delete()
    messages.success(request, "Spareparts Deleted Successfully")
    return redirect('listsp')  