from app.despesas import models
from django.contrib import admin


@admin.register(models.Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'nome')
    list_per_page = 50
