# Generated by Django 4.2 on 2025-02-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absences', '0002_ticket_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='back_hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='back_station',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='commentary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='go_hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='go_station',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
