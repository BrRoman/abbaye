# Generated by Django 4.2 on 2024-11-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imprimerie', '0019_paper_price_full'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='sheets_by_pack',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]