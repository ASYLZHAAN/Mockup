# Generated by Django 3.1.4 on 2021-02-08 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site_food', '0005_remove_good_whatsapp_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='new_price',
            new_name='old_price',
        ),
    ]
