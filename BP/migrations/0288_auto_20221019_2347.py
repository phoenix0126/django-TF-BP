# Generated by Django 3.2.11 on 2022-10-19 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0287_auto_20221019_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_email1', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='email2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_email2', to='BP.contact'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]