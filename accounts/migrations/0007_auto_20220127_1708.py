# Generated by Django 3.2.11 on 2022-01-27 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220127_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='location',
            name='fax',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Fax'),
        ),
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone'),
        ),
        migrations.CreateModel(
            name='OtherLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('fax', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address_type', models.CharField(max_length=255, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_locations', to='accounts.location')),
            ],
        ),
    ]
