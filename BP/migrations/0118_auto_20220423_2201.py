# Generated by Django 3.2.11 on 2022-04-23 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0117_auto_20220423_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litigation',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='litigation_county', to='BP.county'),
        ),
        migrations.AlterField(
            model_name='litigation',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='litigation_states', to='BP.state'),
        ),
    ]
