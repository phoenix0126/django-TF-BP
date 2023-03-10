# Generated by Django 3.2.11 on 2022-01-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney',
            name='favorites',
            field=models.ManyToManyField(related_name='fav_providers', to='accounts.Favorite'),
        ),
        migrations.AlterField(
            model_name='marketer',
            name='favorites',
            field=models.ManyToManyField(related_name='favmarketer_providers', to='accounts.Favorite'),
        ),
    ]
