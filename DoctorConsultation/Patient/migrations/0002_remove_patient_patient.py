# Generated by Django 3.2.9 on 2021-11-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Patient',
        ),
    ]
