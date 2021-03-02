# Generated by Django 3.1.4 on 2021-01-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210122_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='admin_url',
            new_name='construct_url',
        ),
        migrations.RemoveField(
            model_name='site',
            name='client_url',
        ),
        migrations.RemoveField(
            model_name='site',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='site',
            name='information_url',
        ),
        migrations.AddField(
            model_name='site',
            name='template_name',
            field=models.CharField(default='owner/index.html', max_length=380),
            preserve_default=False,
        ),
    ]
