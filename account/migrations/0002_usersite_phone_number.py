# Generated by Django 3.1.4 on 2020-12-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersite',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
