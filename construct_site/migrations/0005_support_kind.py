# Generated by Django 3.1.4 on 2021-02-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site', '0004_remove_support_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='kind',
            field=models.IntegerField(choices=[(1, 'Ватсап'), (2, 'Номер телефона')], default=1),
        ),
    ]
