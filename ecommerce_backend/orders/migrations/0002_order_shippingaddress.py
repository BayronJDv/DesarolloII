# Generated by Django 5.1.3 on 2024-11-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shippingaddress',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
