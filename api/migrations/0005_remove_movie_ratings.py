# Generated by Django 2.1 on 2019-07-08 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190708_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Ratings',
        ),
    ]