# Generated by Django 3.2.11 on 2022-10-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0280_alter_state_stateabr'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='population',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='county',
            name='population_date',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
