# Generated by Django 4.0.3 on 2022-05-18 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_alter_doctor_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='BirthDay',
        ),
    ]
