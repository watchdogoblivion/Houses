# Generated by Django 2.1.1 on 2018-09-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0005_auto_20180905_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='bath',
            new_name='baths',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='floor',
            new_name='floors',
        ),
        migrations.AddField(
            model_name='property',
            name='email',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='phone',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='seller_name',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
    ]