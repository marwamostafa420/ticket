# Generated by Django 4.0.3 on 2022-06-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_alter_patient_national_num_alter_patient_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='National_num',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Phone',
            field=models.CharField(max_length=11),
        ),
    ]
