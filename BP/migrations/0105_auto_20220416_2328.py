# Generated by Django 3.2.11 on 2022-04-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0104_auto_20220416_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseproviders',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='caseproviders',
            name='check_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='caseproviders',
            name='final_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='caseproviders',
            name='ins_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='caseproviders',
            name='reduction',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='caseproviders',
            name='write_off',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
