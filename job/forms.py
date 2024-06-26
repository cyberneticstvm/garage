from django import forms
from .models import Job, JobSparePart, JobService, CustomerSparePart, JobStatus, Account
from django.db.models import Q

class JobForm(forms.ModelForm):
    
    pickup_required = forms.CharField(
        widget=forms.Select(choices={'1': 'Yes', '0': 'No'}),
    )
    pickup_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date',}),
    )
    #status = forms.ModelChoiceField(JobStatus.objects.filter(~Q(status_name='Approved')))
    status = forms.ModelChoiceField(JobStatus.objects.filter())
    staff = forms.ModelChoiceField(Account.objects.filter(is_staff=True))
    
    class Meta:
        model = Job
        fields = ['brand_name', 'model_name', 'make_year', 'color', 'job_description', 'pickup_required', 'pickup_address', 'pickup_date']
        
    def clean(self):
        cleaned_data = super(JobForm, self).clean()
        
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields[field].widget.attrs['placeholder'] = field.replace('_', ' ').title()
            
class JobSparePartsForm(forms.ModelForm):
    
    class Meta:
        model = JobSparePart
        fields = ['spare_part_id', 'qty', 'cost_per_unit',]
        
    def clean(self):
        cleaned_data = super(JobSparePartsForm, self).clean()
        
    def __init__(self, *args, **kwargs):
        super(JobSparePartsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields[field].widget.attrs['placeholder'] = field.replace('_', ' ').title()
            
class JobServiceForm(forms.ModelForm):
    
    class Meta:
        model = JobService
        fields = ['description', 'fee',]
        
    def clean(self):
        cleaned_data = super(JobServiceForm, self).clean()
        
    def __init__(self, *args, **kwargs):
        super(JobServiceForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields[field].widget.attrs['placeholder'] = field.replace('_', ' ').title()

class CustomerSparePartForm(forms.ModelForm):
    
    class Meta:
        model = CustomerSparePart
        fields = ['spare_part_id', 'qty']
        
    def clean(self):
        cleaned_data = super(CustomerSparePartForm, self).clean()
        spare_part_id = self.cleaned_data.get('spare_part_id')
        qty = self.cleaned_data.get('qty')
        if not spare_part_id:
            self._errors['spare_part_name'] = self.error_class([
                'Please select spare part'])
        if not qty:
            self._errors['qty'] = self.error_class([
                'Please enter valid Qty'])
        return cleaned_data
        
    def __init__(self, *args, **kwargs):
        super(CustomerSparePartForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields[field].widget.attrs['placeholder'] = field.replace('_', ' ').title()