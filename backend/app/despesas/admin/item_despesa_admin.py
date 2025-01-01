from app.despesas import models
from django.contrib import admin


@admin.register(models.ItemDespesa)
class ItemDespesaAdmin(admin.ModelAdmin):
    list_display = ('data_da_despesa', 'valor',)
    list_filter = ('data_da_despesa', 'valor', 'created_at', 'updated_at',)
