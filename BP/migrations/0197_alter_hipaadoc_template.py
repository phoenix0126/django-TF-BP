# Generated by Django 3.2.11 on 2022-07-16 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0196_hipaadoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hipaadoc',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HIPAA_doc', to='BP.doc'),
        ),
    ]
