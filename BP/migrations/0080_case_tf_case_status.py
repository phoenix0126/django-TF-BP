# Generated by Django 3.2.11 on 2022-03-26 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0079_auto_20220326_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='tf_case_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tf_case_statuses', to='BP.clientstatus'),
        ),
    ]
