# Generated by Django 3.2.11 on 2022-05-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0134_alter_incidentreport_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChequeRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('cheque_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('cheque_number', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('cleared_on', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('cost', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('for_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_checkrequests', to='BP.case')),
                ('incident_report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BP.incidentreport')),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firm_users_chequerequests', to='BP.attorneystaff')),
            ],
        ),
    ]
