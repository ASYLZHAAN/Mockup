# Generated by Django 3.1.4 on 2021-01-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_phonenumber_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
