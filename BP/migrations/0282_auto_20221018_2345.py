# Generated by Django 3.2.11 on 2022-10-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0281_auto_20221018_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='population',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='county',
            name='population_date',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]