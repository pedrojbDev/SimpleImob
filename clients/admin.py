from django.contrib import admin
from clients.models import Clients

class ClientsAdmin(admin.ModelAdmin):
  list_display= ('name','requirement_neighborhood','requirement_type','requirement_rooms','requirement_suites',)
  search_fields=('name','requirement_neighborhood',)

admin.site.register(Clients,ClientsAdmin)

