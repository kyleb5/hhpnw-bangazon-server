# Generated by Django 4.1.3 on 2024-01-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhpnwapi', '0003_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]