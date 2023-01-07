# Generated by Django 3.2.11 on 2022-08-24 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BP', '0202_emails'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
