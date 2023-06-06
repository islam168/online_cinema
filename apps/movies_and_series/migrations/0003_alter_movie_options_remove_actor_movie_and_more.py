# Generated by Django 4.2.1 on 2023-06-06 04:15

import apps.movies_and_series.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0002_actor_director_tvshow_movie_episode_director_movie_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='tv_shows',
        ),
        migrations.RemoveField(
            model_name='director',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='director',
            name='tv_shows',
        ),
        migrations.AddField(
            model_name='actor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.movies_and_series.utils.upload_instance, verbose_name='Постер'),
        ),
        migrations.AddField(
            model_name='director',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.movies_and_series.utils.upload_instance, verbose_name='Постер'),
        ),
    ]
