# Generated by Django 3.2.18 on 2024-01-10 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imprimerie', '0011_auto_20240110_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='gutter_height',
            new_name='gutters_height',
        ),
        migrations.RenameField(
            model_name='element',
            old_name='gutter_width',
            new_name='gutters_width',
        ),
    ]