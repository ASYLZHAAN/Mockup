# Generated by Django 3.1.4 on 2021-01-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_phonenumber_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='whatsapp_text',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
