# Generated by Django 5.1.4 on 2025-01-01 15:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('descricao', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ManyToManyField(related_name='despesas', to='despesas.categoria')),
                ('user', models.ForeignKey(
                    editable=False, on_delete=models.deletion.CASCADE,
                    related_name='despesas', to=settings.AUTH_USER_MODEL
                    )),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='ItemDespesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_da_despesa', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('despesa', models.ForeignKey(
                    on_delete=models.deletion.CASCADE,
                    related_name='itens', to='despesas.despesa'
                    )),
            ],
            options={
                'verbose_name': 'Item de Despesa',
                'verbose_name_plural': 'Itens de Despesa',
                'ordering': ['-updated_at', '-created_at'],
            },
        ),
    ]
