# Generated by Django 3.2.11 on 2022-07-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0193_auto_20220712_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentgap',
            name='first_date',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='treatmentgap',
            name='second_date',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
