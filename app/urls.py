
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('neighborhood.urls')),
    path('', include('inventory.urls')),
    path('', include('clients.urls')),
    path('notifications/', include('notifications.urls')),
    path('accounts/', include('allauth.urls')),
]
