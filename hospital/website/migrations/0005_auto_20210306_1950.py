# Generated by Django 3.1.5 on 2021-03-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210306_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablee',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
