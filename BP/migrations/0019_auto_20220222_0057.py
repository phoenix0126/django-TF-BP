# Generated by Django 3.2.11 on 2022-02-21 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0018_caraccident'),
    ]

    operations = [
        migrations.AddField(
            model_name='caraccident',
            name='lat',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='caraccident',
            name='long',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
