# Generated by Django 4.0.2 on 2022-03-19 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_customuser_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['uuid']},
        ),
    ]