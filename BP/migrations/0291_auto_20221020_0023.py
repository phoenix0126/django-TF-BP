# Generated by Django 3.2.11 on 2022-10-19 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0290_client_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email1',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone1',
        ),
        migrations.AddField(
            model_name='client',
            name='contact_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_contact1', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_contact2', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_contact3', to='BP.contact'),
        ),
        migrations.AddField(
            model_name='client',
            name='mailing_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_mailing_contact', to='BP.contact'),
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('relationship', models.CharField(blank=True, default='', max_length=100)),
                ('discussCase', models.BooleanField(blank=True, default=False, null=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact', to='BP.contact')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='emergency_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_emergency_contact', to='BP.emergencycontact'),
        ),
    ]
