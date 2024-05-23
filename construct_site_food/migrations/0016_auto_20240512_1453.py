# Generated by Django 3.1.4 on 2024-05-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site_food', '0015_good_font'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='font',
            field=models.CharField(blank=True, choices=[('Arial', 'Arial'), ('Verdana', 'Verdana'), ('Kudry', 'Kudry'), ('Scriptina', 'Scriptina'), ('Edwardian Script', 'Edwardian Script'), ('Great Vibes', 'Great Vibes'), ('Alex Brush', 'Alex Brush'), ('Snell Roundhand', 'Snell Roundhand'), ('Monotype Corsiva', 'Monotype Corsiva'), ('Pinyon Script', 'Pinyon Script'), ('Satisfy', 'Satisfy'), ('Tangerine', 'Tangerine'), ('Allura', 'Allura')], default='AR', max_length=100),
        ),
    ]