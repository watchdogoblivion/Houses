# Generated by Django 2.1.1 on 2018-09-04 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0003_auto_20180903_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='maps_url',
            field=models.CharField(default='NA', max_length=400),
            preserve_default=False,
        ),
    ]