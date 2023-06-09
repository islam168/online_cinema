# Generated by Django 4.2.1 on 2023-06-09 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0020_movie_rating_tvshow_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=10, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='rating',
            field=models.IntegerField(default=10, verbose_name='Рейтинг'),
        ),
    ]
