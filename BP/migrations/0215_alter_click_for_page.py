# Generated by Django 3.2.11 on 2022-09-07 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0214_click_clickidname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='for_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='click_record_page', to='BP.page'),
        ),
    ]
