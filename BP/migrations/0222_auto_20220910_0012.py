# Generated by Django 3.2.11 on 2022-09-09 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0221_alter_case_case_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wu_name', models.CharField(default='', max_length=100)),
                ('table', models.CharField(default='', max_length=100)),
                ('field', models.CharField(default='', max_length=100)),
                ('field_description', models.TextField(blank=True, null=True)),
                ('filled', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('any_all', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('empty', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('valued', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('more', models.CharField(default='', max_length=100)),
                ('less', models.CharField(default='', max_length=100)),
                ('max', models.CharField(default='', max_length=100)),
                ('min', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='case',
            name='auto_case_stage',
            field=models.ManyToManyField(blank=True, related_name='auto_case_stages', to='BP.Stage'),
        ),
        migrations.AlterField(
            model_name='case',
            name='auto_case_status',
            field=models.ManyToManyField(blank=True, related_name='auto_case_statuses', to='BP.Status'),
        ),
        migrations.CreateModel(
            name='ActCaseStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='act_case_status_act', to='BP.act')),
                ('firm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='act_case_status_firm', to='BP.attorney')),
                ('stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='act_case_status_stage', to='BP.stage')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='act_case_status_status', to='BP.status')),
            ],
        ),
        migrations.AddField(
            model_name='act',
            name='work_units',
            field=models.ManyToManyField(blank=True, to='BP.WorkUnit'),
        ),
    ]
