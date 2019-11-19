# Generated by Django 2.2.6 on 2019-11-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='movie',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='movie',
            field=models.ManyToManyField(to='movie.Movie', verbose_name='电影'),
        ),
    ]