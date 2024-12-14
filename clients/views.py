from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from clients.models import Clients
from leads.models import Leads
from clients.forms import ClientsForm
from django.urls import reverse_lazy
from neighborhood.models import Neighborhood
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientsListView(LoginRequiredMixin,ListView):
    model = Clients
    template_name = 'clients_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        lead = self.request.GET.get('lead')
        requirement_rooms = self.request.GET.get('requirement_rooms')
        requirement_value = self.request.GET.get('requirement_value')
        requirement_neighborhood = self.request.GET.get('requirement_neighborhood')
        requirement_garage = self.request.GET.get('requirement_garage')
        requirement_footage = self.request.GET.get('requirement_footage')


        if name:
            queryset = queryset.filter(name__icontains=name)
        if lead:
            queryset = queryset.filter(lead__id=lead)
        if requirement_rooms:
            queryset = queryset.filter(requirement_rooms__icontains=requirement_rooms)
        if requirement_value:
            min_requirement_value, max_requirement_value = map(int, requirement_value.split('-'))
            queryset = queryset.filter(requirement_value__range=(min_requirement_value, max_requirement_value))
        if requirement_neighborhood:
            queryset = queryset.filter(requirement_neighborhood__id=requirement_neighborhood)
        if requirement_footage:
            min_requirement_footage, max_requirement_footage = map(int, requirement_footage.split('-'))
            queryset = queryset.filter(requirement_footage__range=(min_requirement_footage, max_requirement_footage))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leads'] = Leads.objects.all()
        context['requirement_neighborhoods'] = Neighborhood.objects.all()
        context['requirement_footages'] = [
            '100-200',
            '200-300',
            '300-400',
            # Adicione mais ranges conforme necessário
        ]
        context['requirement_values'] = [
            '100000-200000',
            '200000-300000',
            '300000-400000',
            '400000-500000',
            '500000-600000'

            # Adicione mais ranges conforme necessário
        ]
        return context

class ClientsCreateView(LoginRequiredMixin,CreateView):
    model = Clients
    template_name = 'clients_create.html'
    form_class= ClientsForm
    success_url = reverse_lazy('clients_list')

class ClientsDetailView(LoginRequiredMixin,DetailView):
    model = Clients
    template_name = 'clients_detail.html'

class ClientsUpdateView(LoginRequiredMixin,UpdateView):
    model = Clients
    template_name = 'clients_update.html'
    success_url = reverse_lazy('clients_list')
    form_class= ClientsForm

class ClientsDeleteView(LoginRequiredMixin,DeleteView):
    model = Clients
    template_name = 'clients_delete.html'
    success_url = reverse_lazy('clients_list')