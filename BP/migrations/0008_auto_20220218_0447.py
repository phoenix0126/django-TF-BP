# Generated by Django 3.2.11 on 2022-02-17 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0007_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='case_type',
        ),
        migrations.RemoveField(
            model_name='client',
            name='incident_date',
        ),
        migrations.AddField(
            model_name='notes',
            name='for_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BP.client'),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_date', models.CharField(default='', max_length=100)),
                ('case_type', models.CharField(default='', max_length=100)),
                ('case_category', models.CharField(default='', max_length=100, null=True)),
                ('for_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_cases', to='BP.client')),
            ],
        ),
    ]
