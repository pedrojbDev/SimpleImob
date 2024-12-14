from django import forms
from . import models


class InventoryForm(forms.ModelForm):

    class Meta:
        model = models.Inventory
        fields = ['title', 'type', 'rooms','footage', 'suites', 'garage', 'neighborhood', 'street','value','modality','owner_name','owner_tel','comission','description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'neighborhood': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'modality': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'owner_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'footage': forms.NumberInput(attrs={'class': 'form-control'}),
            'garage': forms.NumberInput(attrs={'class': 'form-control'}),
            'suites': forms.NumberInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comission': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'footage':'Metragem',
            'type': 'Tipo',
            'rooms': 'Quartos',
            'suites': 'Suites',
            'garage': 'Garagem',
            'neighborhood': 'Bairro',
            'street': 'Rua',
            'value': 'Valor',
            'modality': 'Modalidade',
            'owner_name': 'Nome do Dono',
            'owner_tel': 'Numero do Dono',
            'comission': 'Comissao',
            'description': 'Descricao',
        }