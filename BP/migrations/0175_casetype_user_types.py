# Generated by Django 3.2.11 on 2022-05-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP', '0174_auto_20220523_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='casetype',
            name='user_types',
            field=models.ManyToManyField(related_name='casetypes_usertypes', to='BP.AttorneyUserType'),
        ),
    ]
