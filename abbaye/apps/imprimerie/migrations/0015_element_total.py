# Generated by Django 3.2.18 on 2024-01-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imprimerie', '0014_auto_20240110_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
