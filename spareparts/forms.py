from django import forms
from .models import Spareparts

class SparepartsForm(forms.ModelForm):
    class Meta:
        model = Spareparts
        fields = ['spare_part_name', 'cost_per_unit']
        
    def clean(self):
        cleaned_data = super(SparepartsForm, self).clean()
        
    def __init__(self, *args, **kwargs):
        super(SparepartsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields[field].widget.attrs['placeholder'] = field.replace('_', ' ').title()