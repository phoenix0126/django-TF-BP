# Generated by Django 3.2.11 on 2022-05-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0143_check_for_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorneystaff',
            name='accounting_admin_permission',
            field=models.CharField(blank=True, default='False', max_length=255, null=True),
        ),
    ]
