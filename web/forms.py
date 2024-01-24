from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, label='User Name')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'