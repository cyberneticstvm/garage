from django import forms
from .models import Spareparts

class SparepartsForm(forms.ModelForm):
    class Meta:
        model = Spareparts
        fields = ['spare_part_name', 'cost_per_unit']
        
    def clean(self):
        cleaned_data = super(SparepartsForm, self).clean()
        spare_part_name = self.cleaned_data.get('username')
        cost_per_unit = self.cleaned_data.get('text')
        if len(spare_part_name) < 5:
            self._errors['spare_part_name'] = self.error_class([
                'Minimum 5 characters required'])
        if cost_per_unit < 1 or cost_per_unit == '':
            self._errors['cost_per_unit'] = self.error_class([
                'Amount should be valid'])
        return cleaned_data
        
    def __init__(self, *args, **kwargs):
        super(SparepartsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields[field].widget.attrs['placeholder'] = field.replace('_', ' ').title()