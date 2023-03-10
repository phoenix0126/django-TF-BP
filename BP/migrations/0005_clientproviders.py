# Generated by Django 3.2.11 on 2022-02-16 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_specialty_secondary_color'),
        ('BP', '0004_client_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProviders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bp_client_providers', to='BP.client')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bp_provider_location', to='accounts.location')),
                ('specialty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bp_provider_specialty', to='accounts.specialty')),
            ],
        ),
    ]
