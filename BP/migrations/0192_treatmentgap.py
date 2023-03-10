# Generated by Django 3.2.11 on 2022-07-12 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0191_clickrecord_for_firm'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentGap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('second_date', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('days', models.IntegerField(blank=True, default=0, null=True)),
                ('doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tf_gap_doc', to='BP.doc')),
                ('for_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tf_gap_case', to='BP.case')),
            ],
        ),
    ]
