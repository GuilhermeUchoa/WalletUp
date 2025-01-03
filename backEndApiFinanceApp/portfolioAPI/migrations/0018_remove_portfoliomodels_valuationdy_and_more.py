# Generated by Django 5.0.6 on 2025-01-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioAPI', '0017_portfoliomodels_dy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliomodels',
            name='valuationDy',
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='metaDy',
            field=models.FloatField(blank=True, null=True),
        ),
    ]