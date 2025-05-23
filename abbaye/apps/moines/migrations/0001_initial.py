# Generated by Django 3.2.25 on 2025-03-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('entry', models.DateField()),
                ('rank_entry', models.SmallIntegerField(default=1)),
                ('habit', models.DateField(blank=True, null=True)),
                ('profession_temp', models.DateField(blank=True, null=True)),
                ('profession_perp', models.DateField(blank=True, null=True)),
                ('priest', models.DateField(blank=True, null=True)),
                ('death', models.DateField(blank=True, null=True)),
                ('feast_day', models.IntegerField()),
                ('feast_month', models.IntegerField()),
                ('laundry_number', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('additional_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('absolute_rank', models.IntegerField(default=4)),
                ('is_abbot', models.BooleanField(default=False)),
                ('is_prior', models.BooleanField(default=False)),
                ('is_abbot_emerite', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('absences_recipient', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
