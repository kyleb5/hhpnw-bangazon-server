# Generated by Django 4.1.3 on 2024-01-12 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhpnwapi', '0006_ordermenuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('tipAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paymentType', models.CharField(max_length=12)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhpnwapi.orders')),
            ],
        ),
    ]
