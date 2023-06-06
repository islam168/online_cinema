# Generated by Django 4.2.1 on 2023-06-06 19:46

import apps.movies_and_series.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0009_episode_poster_episode_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='trailer',
            field=models.FileField(upload_to=apps.movies_and_series.utils.videos_uploaded, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Трайлер эпизода'),
        ),
    ]