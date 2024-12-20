# Generated by Django 3.2.18 on 2023-03-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('shortcut', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('sound', models.TextField(null=True)),
                ('sound_description', models.TextField(null=True)),
                ('where', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
