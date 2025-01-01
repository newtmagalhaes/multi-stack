from django.db import models


class ItemDespesa(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_da_despesa = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    despesa = models.ForeignKey('Despesa', on_delete=models.CASCADE, related_name='itens')

    class Meta:
        verbose_name = 'Item de Despesa'
        verbose_name_plural = 'Itens de Despesa'
        ordering = ['-updated_at', '-created_at']
