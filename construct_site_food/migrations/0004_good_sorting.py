# Generated by Django 3.1.4 on 2021-02-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site_food', '0003_delete_additionaldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='sorting',
            field=models.IntegerField(default=0),
        ),
    ]
