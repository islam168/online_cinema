# Generated by Django 4.2.1 on 2023-06-09 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_and_series', '0019_rename_episode_episode_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]
