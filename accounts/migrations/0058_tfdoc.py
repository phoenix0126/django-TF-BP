# Generated by Django 3.2.11 on 2022-06-28 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0057_auto_20220629_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='TFDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(null=True, upload_to='images/')),
                ('file_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('page_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('document_no', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('check', models.CharField(blank=True, default='False', max_length=255, null=True)),
                ('for_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_tf_accounting_doc', to='accounts.provider')),
                ('for_tf_accounting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tf_accounting_doc', to='accounts.tfaccounting')),
            ],
        ),
    ]
