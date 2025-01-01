# Generated by Django 5.0.6 on 2024-12-06 11:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.CharField(max_length=250, unique=True)),
                ('cotacao', models.FloatField(blank=True, null=True)),
                ('quantidade', models.FloatField(blank=True, default=0, null=True)),
                ('valor', models.FloatField(blank=True, default=0, null=True)),
                ('porcentagem', models.FloatField(blank=True, null=True)),
                ('variacaoAnual', models.FloatField(blank=True, null=True)),
                ('meta', models.FloatField(blank=True, null=True)),
                ('dy', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[('comprar', 'comprar'), ('aguardar', 'aguardar'), ('vender', 'vender')], default='comprar', max_length=250)),
                ('tipo', models.CharField(choices=[('acao', 'acao'), ('bdr', 'bdr'), ('fii', 'fii'), ('rendaFixa', 'rendaFixa')], max_length=250)),
                ('aporte', models.IntegerField(blank=True, default=0, null=True)),
                ('precoMedio', models.FloatField(blank=True, null=True)),
                ('valuationDy', models.FloatField(blank=True, null=True)),
                ('valuationDFC', models.FloatField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'ativo')},
            },
        ),
    ]
