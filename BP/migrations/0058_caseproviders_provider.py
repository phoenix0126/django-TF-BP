# Generated by Django 3.2.11 on 2022-03-11 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_auto_20220311_2216'),
        ('BP', '0057_auto_20220311_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseproviders',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.provider'),
        ),
    ]
