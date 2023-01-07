# Generated by Django 3.2.11 on 2022-02-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=100)),
                ('age', models.IntegerField(default='')),
                ('incident_date', models.CharField(default='', max_length=100)),
                ('case_type', models.CharField(default='', max_length=100)),
            ],
        ),
    ]