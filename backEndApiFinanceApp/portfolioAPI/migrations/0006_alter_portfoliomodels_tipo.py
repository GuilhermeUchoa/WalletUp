# Generated by Django 5.0.6 on 2024-12-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioAPI', '0005_alter_portfoliomodels_cotacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodels',
            name='tipo',
            field=models.CharField(choices=[('Acoes', 'Acoes'), ('Brazilian Depositary Receipts', 'Brazilian Depositary Receipts'), ('Fundo de Investimento', 'Fundo de Investimento'), ('Tesouro Direto', 'Tesouro Direto')], max_length=250),
        ),
    ]
