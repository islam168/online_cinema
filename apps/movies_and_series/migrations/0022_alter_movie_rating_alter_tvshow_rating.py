# Generated by Django 4.2.1 on 2023-06-09 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0021_alter_movie_rating_alter_tvshow_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=10, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='rating',
            field=models.FloatField(default=10, verbose_name='Рейтинг'),
        ),
    ]