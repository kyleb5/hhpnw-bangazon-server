# Generated by Django 4.1.3 on 2024-01-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhpnwapi', '0007_revenue'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField()),
                ('joinDate', models.IntegerField()),
                ('hasAccess', models.BooleanField()),
            ],
        ),
    ]
