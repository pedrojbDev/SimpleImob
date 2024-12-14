from django.urls import path
from . import views

urlpatterns = [
    path('',views.InventoryListView.as_view(),name='inventory_list'),
    path('inventory/<int:pk>/detail/',views.InventoryDetailView.as_view(),name='inventory_detail'),
    path('inventory/create/',views.InventoryCreateView.as_view(),name='inventory_create'),
    path('inventory/<int:pk>/update/',views.InventoryUpdateView.as_view(),name='inventory_update'),
    path('inventory/<int:pk>/delete/',views.InventoryDeleteView.as_view(),name='inventory_delete'),
]