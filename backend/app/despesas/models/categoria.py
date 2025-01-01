from django.db import models


class Categoria(models.Model):
    nome = models.CharField(
        max_length=255, unique=True, blank=False, null=False,
    )
    descricao = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # despesas: Manager[Despesa]

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']
