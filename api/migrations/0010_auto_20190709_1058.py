# Generated by Django 2.1 on 2019-07-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_movie_totalseasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
