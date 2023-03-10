# Generated by Django 3.2.11 on 2022-05-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0169_requestupdate_request_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('case_types', models.ManyToManyField(related_name='casestage_types', to='BP.ClientStatus')),
            ],
        ),
    ]
