# Generated by Django 3.2.11 on 2022-03-07 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0052_alter_attorney_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='invoice_number',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
