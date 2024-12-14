import locale
from django.db import models
from type.models import Type
from neighborhood.models import Neighborhood
from modality.models import Modality

class Inventory(models.Model):
    title = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.PROTECT,related_name='inventory')
    rooms = models.IntegerField()
    suites = models.IntegerField()
    footage = models.IntegerField(blank=True,null=True)
    garage = models.IntegerField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.PROTECT)
    street = models.CharField(max_length=200)
    value = models.DecimalField(decimal_places=2,max_digits=20)
    modality = models.ForeignKey(Modality,on_delete=models.PROTECT)
    owner_name = models.CharField(max_length=50)
    owner_tel = models.CharField(max_length=25)
    comission = models.DecimalField(decimal_places=2,max_digits=20)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_properties = models.IntegerField(default=1)


    class Meta:
      ordering = ['title']
    
    def formatted_value(self):
        # Configura o locale para o padrão do sistema
        locale.setlocale(locale.LC_ALL, '')
        # Formate o valor para o padrão desejado, por exemplo:
        formatted_value = locale.currency(self.value, grouping=True)
        return formatted_value

    def __str__(self):
        return self.title




