from django.shortcuts import render, redirect
from .forms import JobForm

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            return redirect('create')
    else:
        form = JobForm()
    context = {'form': form,}
    return render(request, 'customer/job.html', context)
