# Generated by Django 3.1.4 on 2021-01-29 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20210129_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='slug',
        ),
    ]
