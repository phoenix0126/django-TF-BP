# Generated by Django 3.2.11 on 2022-07-16 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0195_treatmentgap_for_case_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='HIPAADoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_value', models.CharField(default='', max_length=255, null=True)),
                ('y_value', models.CharField(default='', max_length=255, null=True)),
                ('for_firm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='HIPAA_for_atttorney', to='BP.attorney')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='HIPAA_doc', to='BP.doc')),
            ],
        ),
    ]