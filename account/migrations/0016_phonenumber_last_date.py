# Generated by Django 3.1.4 on 2021-01-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_delete_currentsupportphonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
