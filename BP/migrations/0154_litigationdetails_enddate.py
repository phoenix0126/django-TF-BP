# Generated by Django 3.2.11 on 2022-05-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0153_litigationdetails_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='litigationdetails',
            name='endDate',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]