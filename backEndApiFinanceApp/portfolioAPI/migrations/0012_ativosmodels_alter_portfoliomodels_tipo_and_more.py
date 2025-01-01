# Generated by Django 5.0.6 on 2025-01-01 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioAPI', '0011_rename_question00_portfoliomodels_question0_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtivosModels',
            fields=[
                ('ativoPrincipal', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cotacao', models.FloatField(default=0)),
                ('tipo', models.CharField(choices=[('Acoes', 'Acoes'), ('Brazilian Depositary Receipts', 'Brazilian Depositary Receipts'), ('Fundo de Investimento', 'Fundo de Investimento'), ('Tesouro Direto', 'Tesouro Direto'), ('Outros', 'Outros')], default='Outros', max_length=250)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='portfoliomodels',
            name='tipo',
            field=models.CharField(choices=[('Acoes', 'Acoes'), ('Brazilian Depositary Receipts', 'Brazilian Depositary Receipts'), ('Fundo de Investimento', 'Fundo de Investimento'), ('Tesouro Direto', 'Tesouro Direto'), ('Outros', 'Outros')], max_length=250),
        ),
        migrations.AlterField(
            model_name='portfoliomodels',
            name='ativo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioAPI.ativosmodels'),
        ),
    ]
