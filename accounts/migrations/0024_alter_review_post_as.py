# Generated by Django 3.2.11 on 2022-01-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_marketerlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='post_as',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
