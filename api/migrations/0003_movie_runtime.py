# Generated by Django 2.1 on 2019-07-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190708_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Runtime',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
