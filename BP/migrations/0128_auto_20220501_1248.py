# Generated by Django 3.2.11 on 2022-05-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0127_auto_20220501_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed_note',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='notes',
            field=models.CharField(blank=True, default='N/A', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(blank=True, default='Not Completed', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_type',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
