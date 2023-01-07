# Generated by Django 3.2.11 on 2022-02-01 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20220131_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketer',
            name='marketer_code',
        ),
        migrations.CreateModel(
            name='MarketerCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='marketer_code', to='accounts.marketer')),
            ],
        ),
        migrations.AddField(
            model_name='attorney',
            name='marketer_codes',
            field=models.ManyToManyField(related_name='attorney_mark_code', to='accounts.MarketerCode'),
        ),
    ]