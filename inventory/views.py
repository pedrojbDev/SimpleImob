from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from inventory.models import Inventory
from neighborhood.models import Neighborhood
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

class InventoryListView(LoginRequiredMixin,ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset()
        rooms = self.request.GET.get('rooms')
        value = self.request.GET.get('value')
        neighborhood = self.request.GET.get('neighborhood')
        garage = self.request.GET.get('garage')
        footage = self.request.GET.get('footage')

        
        if rooms:
            queryset = queryset.filter(rooms__icontains=rooms)
        if value:
            min_value, max_value = map(int, value.split('-'))
            queryset = queryset.filter(value__range=(min_value, max_value))
        if neighborhood:
            queryset = queryset.filter(neighborhood__id=neighborhood)
        if footage:
            min_footage, max_footage = map(int, footage.split('-'))
            queryset = queryset.filter(footage__range=(min_footage, max_footage))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['neighborhoods'] = Neighborhood.objects.all()
        context['footages'] = [
            '100-200',
            '200-300',
            '300-400',
            # Adicione mais ranges conforme necessário
        ]
        context['values'] = [
            '100000-200000',
            '200000-300000',
            '300000-400000',
            '400000-500000',
            '500000-600000'

            # Adicione mais ranges conforme necessário
        ]
        return context

class InventoryDetailView(LoginRequiredMixin,DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'

class InventoryCreateView(LoginRequiredMixin,CreateView):
    model = Inventory
    template_name = 'inventory_create.html'
    form_class = forms.InventoryForm
    success_url = reverse_lazy('inventory_list')

class InventoryUpdateView(LoginRequiredMixin,UpdateView):
    model = Inventory
    template_name = 'inventory_update.html'
    form_class = forms.InventoryForm
    success_url = reverse_lazy('inventory_list')

class InventoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Inventory
    template_name = 'inventory_delete.html'
    success_url = reverse_lazy('inventory_list')




    
    

        
        




