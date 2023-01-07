# Generated by Django 3.2.11 on 2022-02-23 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0025_treatmentnote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='total_visits',
        ),
        migrations.RemoveField(
            model_name='case',
            name='visit_from',
        ),
        migrations.RemoveField(
            model_name='case',
            name='visit_to',
        ),
        migrations.AddField(
            model_name='caseproviders',
            name='total_visits',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='caseproviders',
            name='visit_from',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='caseproviders',
            name='visit_to',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
