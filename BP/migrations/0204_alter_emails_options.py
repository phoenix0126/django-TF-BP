# Generated by Django 3.2.11 on 2022-08-24 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0203_client_client_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emails',
            options={'ordering': ['-created_at']},
        ),
    ]
