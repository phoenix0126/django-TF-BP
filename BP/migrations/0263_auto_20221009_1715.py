# Generated by Django 3.2.11 on 2022-10-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0262_auto_20221009_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherparty',
            name='other_party_insurance',
            field=models.ManyToManyField(blank=True, to='BP.Insurance'),
        ),
        migrations.AlterField(
            model_name='otherparty',
            name='party_first_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='otherparty',
            name='party_last_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='otherparty',
            name='party_middle_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
