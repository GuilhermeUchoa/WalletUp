# Generated by Django 5.0.6 on 2024-12-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioAPI', '0009_alter_questionarioqualitativoforms_question00_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodels',
            name='question00',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question01',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question02',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question03',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question04',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question05',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question06',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question07',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question08',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question09',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question10',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='portfoliomodels',
            name='question11',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='QuestionarioQualitativoForms',
        ),
    ]
