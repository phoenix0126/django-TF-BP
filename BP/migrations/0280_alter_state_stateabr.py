# Generated by Django 3.2.11 on 2022-10-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0279_state_stateabr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='StateAbr',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
