# Generated by Django 3.1.4 on 2021-03-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site_food', '0011_auto_20210208_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
