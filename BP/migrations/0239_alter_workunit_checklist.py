# Generated by Django 3.2.11 on 2022-09-16 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0238_workunit_checklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workunit',
            name='checklist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BP.checklist'),
        ),
    ]