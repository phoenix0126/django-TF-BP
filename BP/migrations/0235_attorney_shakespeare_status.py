# Generated by Django 3.2.11 on 2022-09-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0234_case_property_damage_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney',
            name='shakespeare_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
