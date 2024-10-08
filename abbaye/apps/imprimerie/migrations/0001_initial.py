# Generated by Django 3.2.18 on 2023-12-18 09:34

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('address3', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_quill.fields.QuillField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dim1', models.CharField(max_length=3)),
                ('dim2', models.CharField(max_length=3)),
                ('weight', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imprimerie.client')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, choices=[('CMYN', 'CMYN'), ('B&W', 'B&W')], max_length=255, null=True)),
                ('paper_cut_into', models.IntegerField(blank=True, null=True)),
                ('paper_dim1_machine', models.FloatField(blank=True, null=True)),
                ('paper_dim2_machine', models.FloatField(blank=True, null=True)),
                ('file_width', models.FloatField(blank=True, null=True)),
                ('file_height', models.FloatField(blank=True, null=True)),
                ('imposition', models.IntegerField(blank=True, null=True)),
                ('number_of_sheets_doc', models.IntegerField(blank=True, null=True)),
                ('recto_verso', models.BooleanField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imprimerie.paper')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imprimerie.project')),
            ],
        ),
    ]
