# Generated by Django 3.1.4 on 2021-02-17 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site', '0003_support_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='support',
            name='kind',
        ),
    ]