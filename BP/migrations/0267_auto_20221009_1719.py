# Generated by Django 3.2.11 on 2022-10-09 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0266_auto_20221009_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherparty',
            name='party_contact_last',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='otherparty_last_contact', to='BP.contact'),
        ),
        migrations.AlterField(
            model_name='otherparty',
            name='party_home_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='otherparty_home_contact', to='BP.contact'),
        ),
    ]
