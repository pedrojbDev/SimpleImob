from django.contrib import admin
from . import models

class ModalityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(models.Modality,ModalityAdmin)
