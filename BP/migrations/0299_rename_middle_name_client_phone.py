# Generated by Django 3.2.11 on 2022-10-24 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0298_auto_20221025_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='middle_name',
            new_name='phone',
        ),
    ]
