# Generated by Django 3.2.11 on 2022-01-28 10:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20220127_1708'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Provider',
        ),
    ]
