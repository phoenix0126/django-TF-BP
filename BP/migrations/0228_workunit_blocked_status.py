# Generated by Django 3.2.11 on 2022-09-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0227_auto_20220910_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='workunit',
            name='blocked_status',
            field=models.ManyToManyField(blank=True, null=True, related_name='blocked_status_wu', to='BP.Status'),
        ),
    ]
