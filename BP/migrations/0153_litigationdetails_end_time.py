# Generated by Django 3.2.11 on 2022-05-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0152_statute_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='litigationdetails',
            name='end_time',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]