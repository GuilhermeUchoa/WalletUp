# Generated by Django 5.0.6 on 2025-01-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioAPI', '0012_ativosmodels_alter_portfoliomodels_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodels',
            name='tipo',
            field=models.CharField(choices=[('Acoes', 'Acoes'), ('Brazilian Depositary Receipts', 'Brazilian Depositary Receipts'), ('Fundo de Investimento', 'Fundo de Investimento'), ('Tesouro Direto', 'Tesouro Direto'), ('Outros', 'Outros')], editable=False, max_length=250),
        ),
    ]
