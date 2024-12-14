from django.db import models
from leads.models import Leads
from type.models import Type
from neighborhood.models import Neighborhood
from modality.models import Modality

import locale


class Clients(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    email = models.EmailField(blank=True,null=True)
    lead = models.ForeignKey(Leads, on_delete=models.PROTECT)
    requirement_type = models.ForeignKey(Type, on_delete=models.PROTECT,related_name='clients')
    requirement_rooms = models.IntegerField()
    requirement_footage = models.IntegerField(blank=True,null=True)
    requirement_suites = models.IntegerField()
    requirement_garage = models.IntegerField()
    requirement_neighborhood = models.ForeignKey(Neighborhood,on_delete=models.PROTECT)
    requirement_value = models.DecimalField(decimal_places=2,max_digits=20)
    requirement_modality = models.ForeignKey(Modality,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['name']
    
    def formatted_value(self):
        # Configura o locale para o padrão do sistema
        locale.setlocale(locale.LC_ALL, '')
        # Formate o valor para o padrão desejado, por exemplo:
        formatted_value = locale.currency(self.requirement_value, grouping=True)
        return formatted_value

    def __str__(self):
        return self.name
    




