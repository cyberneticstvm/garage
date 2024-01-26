from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    
    pickup_required = forms.CharField(
        widget=forms.Select(choices={'1': 'Yes', '0': 'No'}),
    )
    
    class Meta:
        model = Job
        fields = ['brand_name', 'model_name', 'make_year', 'color', 'job_description', 'pickup_required', 'pickup_address']
        
    def clean(self):
        cleaned_data = super(JobForm, self).clean()
        
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields[field].widget.attrs['placeholder'] = field.replace('_', ' ').title()