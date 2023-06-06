# Generated by Django 4.2.1 on 2023-06-06 04:59

import apps.movies_and_series.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0003_alter_movie_options_remove_actor_movie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.movies_and_series.utils.upload_instance, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='director',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.movies_and_series.utils.upload_instance, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(blank=True, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Фильм'),
        ),
    ]