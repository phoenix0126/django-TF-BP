# Generated by Django 3.2.11 on 2022-02-18 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0010_auto_20220218_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_status',
            field=models.CharField(default='New Lead', max_length=100, null=True),
        ),
    ]
