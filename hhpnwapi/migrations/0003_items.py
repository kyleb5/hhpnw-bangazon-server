# Generated by Django 4.1.3 on 2024-01-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhpnwapi', '0002_alter_orders_customerphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('img', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
