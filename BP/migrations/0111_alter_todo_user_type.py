# Generated by Django 3.2.11 on 2022-04-19 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0110_alter_notes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Todo_usertypes', to='BP.attorneyusertype'),
        ),
    ]