# Generated by Django 3.2.11 on 2022-10-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0267_auto_20221009_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='witness',
            name='witness_insurance',
            field=models.ManyToManyField(blank=True, to='BP.Insurance'),
        ),
        migrations.AlterField(
            model_name='witness',
            name='age',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='witness',
            name='driver_license',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='witness',
            name='ssn',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='witness',
            name='witness_first_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='witness',
            name='witness_last_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='witness',
            name='witness_middle_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='witness',
            name='witness_note',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
