# Generated by Django 3.2.11 on 2022-03-26 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0078_auto_20220326_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casechecklist',
            name='checklist',
        ),
        migrations.AddField(
            model_name='casechecklist',
            name='checklist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orignalchecklist_case', to='BP.checklist'),
        ),
    ]
