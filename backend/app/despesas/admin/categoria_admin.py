from app.despesas import models
from django.contrib import admin


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')
    list_filter = ('created_at')
