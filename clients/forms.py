from django import forms
from . import models


class ClientsForm(forms.ModelForm):

    class Meta:
        model = models.Clients
        fields = ['name', 'requirement_type', 'requirement_rooms','requirement_footage', 'requirement_suites', 'requirement_garage', 'requirement_neighborhood','requirement_value','requirement_modality','tel','email','lead']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'requirement_neighborhood': forms.Select(attrs={'class': 'form-control'}),
            'requirement_type': forms.Select(attrs={'class': 'form-control'}),
            'requirement_modality': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'requirement_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'requirement_footage': forms.NumberInput(attrs={'class': 'form-control'}),
            'requirement_garage': forms.NumberInput(attrs={'class': 'form-control'}),
            'requirement_suites': forms.NumberInput(attrs={'class': 'form-control'}),
            'requirement_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'lead': forms.Select(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'name': 'Nome',
            'requirement_footage':'Metragem',
            'requirement_type': 'Tipo',
            'requirement_rooms': 'Quartos',
            'requirement_suites': 'Suites',
            'requirement_garage': 'Garagem',
            'requirement_neighborhood': 'Bairro',
            
            'requirement_value': 'Valor',
            'requirement_modality': 'Modalidade',
            
            'tel': 'Numero do Dono',
            'email': 'Email',
            'lead': 'Lead',
        }