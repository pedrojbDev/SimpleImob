from allauth.account.forms import SignupForm,LoginForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # Adiciona a classe 'form-control' a todos os campos do formulário
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        # Adiciona a classe 'form-control' a todos os campos do formulário, exceto o 'remember'
        for field_name, field in self.fields.items():
            if field_name != 'remember':
                field.widget.attrs['class'] = 'form-control'