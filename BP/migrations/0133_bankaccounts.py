# Generated by Django 3.2.11 on 2022-05-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0132_auto_20220503_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('account_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('account_number', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
