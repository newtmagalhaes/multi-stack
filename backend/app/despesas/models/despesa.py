from django.contrib.auth import get_user_model
from django.db import models

_User = get_user_model()


class Despesa(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=255)
    descricao = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    categorias = models.ManyToManyField('Categoria', related_name='despesas')
    user = models.ForeignKey(
        _User, on_delete=models.CASCADE, related_name='despesas',
        editable=False,
    )
    # itens: Manager[ItemDespesa]

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        ordering = ['nome']
