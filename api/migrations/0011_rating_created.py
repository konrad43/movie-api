# Generated by Django 2.1 on 2019-07-09 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190709_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
