# Generated by Django 2.1.1 on 2018-09-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0002_auto_20180903_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image_url',
            field=models.CharField(max_length=400),
        ),
    ]
