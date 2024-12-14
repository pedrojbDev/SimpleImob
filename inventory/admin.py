from django.contrib import admin
from inventory.models import Inventory

class InventoryAdmin(admin.ModelAdmin):
  list_display= ('title','neighborhood','type','rooms','suites',)
  search_fields=('title','neighborhood',)

admin.site.register(Inventory,InventoryAdmin)


