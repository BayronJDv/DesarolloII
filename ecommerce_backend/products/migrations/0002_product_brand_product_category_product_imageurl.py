# Generated by Django 5.1.3 on 2024-11-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='tripleA', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='imageurl',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
