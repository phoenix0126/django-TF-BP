# Generated by Django 3.2.11 on 2022-07-12 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0194_auto_20220713_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentgap',
            name='for_case_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tf_gap_case_providers', to='BP.caseproviders'),
        ),
    ]
