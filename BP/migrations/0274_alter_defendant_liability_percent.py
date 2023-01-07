# Generated by Django 3.2.11 on 2022-10-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0273_auto_20221016_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defendant',
            name='liability_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
