from django.urls import path
from . import views

urlpatterns = [
    path('clients/list/',views.ClientsListView.as_view(),name='clients_list'),
    path('clients/create/',views.ClientsCreateView.as_view(),name='clients_create'),
    path('clients/<int:pk>/detail/',views.ClientsDetailView.as_view(),name='clients_detail'),
    path('clients/<int:pk>/update/',views.ClientsUpdateView.as_view(),name='clients_update'),
    path('clients/<int:pk>/delete/',views.ClientsDeleteView.as_view(),name='clients_delete'),
]