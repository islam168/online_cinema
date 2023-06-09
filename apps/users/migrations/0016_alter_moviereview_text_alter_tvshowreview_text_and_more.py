# Generated by Django 4.2.1 on 2023-06-09 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0020_movie_rating_tvshow_rating'),
        ('users', '0015_subscription_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='text',
            field=models.CharField(blank=True, max_length=512, verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='tvshowreview',
            name='text',
            field=models.CharField(blank=True, max_length=512, verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='tvshowreview',
            name='tvshow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tvshowreview', to='movies_and_series.tvshow', verbose_name='Сериал'),
        ),
    ]
