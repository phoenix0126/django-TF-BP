# Generated by Django 3.2.11 on 2022-02-17 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_specialty_secondary_color'),
        ('BP', '0008_auto_20220218_0447'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseProviders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bp_case_providers', to='BP.case')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bp_provider_location', to='accounts.location')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bp_provider_specialty', to='accounts.specialty')),
            ],
        ),
        migrations.DeleteModel(
            name='ClientProviders',
        ),
    ]